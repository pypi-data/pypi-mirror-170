"""Unit tests for BazaarClient."""

from __future__ import unicode_literals

import os
import unittest
from hashlib import md5

import six

from rbtools.clients import RepositoryInfo
from rbtools.clients.bazaar import BazaarClient
from rbtools.clients.errors import TooManyRevisionsError
from rbtools.clients.tests import FOO, FOO1, FOO2, FOO3, SCMClientTestCase
from rbtools.utils.checks import check_install
from rbtools.utils.filesystem import make_tempdir
from rbtools.utils.process import execute


class BazaarClientTests(SCMClientTestCase):
    """Unit tests for BazaarClient."""

    @classmethod
    def setup_checkout(cls, checkout_dir):
        """Populate two Bazaar clones.

        This will create a clone of the sample Bazaar repository stored in
        the :file:`testdata` directory, and a child clone of that first
        clone.

        Args:
            checkout_dir (unicode):
                The top-level directory in which clones will be placed.

        Returns:
            The main clone directory, or ``None`` if :command:`bzr` isn't
            in the path.
        """
        original_branch = os.path.join(checkout_dir, 'orig')
        child_branch = os.path.join(checkout_dir, 'child')

        os.mkdir(checkout_dir, 0o700)
        os.mkdir(original_branch, 0o700)
        os.mkdir(child_branch, 0o700)

        cls.original_branch = original_branch
        cls.child_branch = child_branch

        if check_install(['bzr', 'help']):
            cls._bzr = 'bzr'
        elif check_install(['brz', 'help']):
            cls._bzr = 'brz'
        else:
            cls._bzr = None

        if cls._bzr:
            try:
                cls._run_bzr(['init', '.'], cwd=original_branch)
                cls._bzr_add_file_commit(filename='foo.txt',
                                         data=FOO,
                                         msg='initial commit',
                                         cwd=original_branch)

                cls._run_bzr(['branch', '--use-existing-dir', original_branch,
                              child_branch],
                             cwd=original_branch)
            except Exception as e:
                # We couldn't set up the repository, so skip this. We'll skip
                # when setting up the client.
                pass

        return original_branch

    def setUp(self):
        if not self._bzr:
            raise unittest.SkipTest('bzr not found in path')

        super(BazaarClientTests, self).setUp()

        self.set_user_home(os.path.join(self.testdata_dir, 'homedir'))

        self.options.parent_branch = None
        self.client = BazaarClient(options=self.options)

    @classmethod
    def _run_bzr(cls, command, *args, **kwargs):
        """Run Bazaar/Breezy with the provided arguments.

        Args:
            command (list of unicode):
                The argument to pass to the command.

            *args (tuple):
                Additional positional arguments to pass to
                :py:func:`~rtools.utils.process.execute`.

            **kwargs (dict):
                Additional Keyword arguments to pass to
                :py:func:`~rtools.utils.process.execute`.

        Returns:
            object:
            The result of the :py:func:`~rtools.utils.process.execute` call.
        """
        return execute(
            [cls._bzr] + command,
            env={
                'BRZ_EMAIL': 'Test User <test@example.com>',
                'BZR_EMAIL': 'Test User <test@example.com>',
            },
            *args,
            **kwargs)

    @classmethod
    def _bzr_add_file_commit(cls, filename, data, msg, cwd=None, *args,
                             **kwargs):
        """Add a file to a Bazaar repository.

        Args:
            filename (unicode):
                The name of the file to add.

            data (bytes):
                The data to write to the file.

            msg (unicode):
                The commit message to use.

            cwd (unicode, optional):
                A working directory to use when running the bzr commands.

            *args (list):
                Positional arguments to pass through to
                :py:func:`rbtools.utils.process.execute`.

            **kwargs (dict):
                Keyword arguments to pass through to
                :py:func:`rbtools.utils.process.execute`.
        """
        if cwd is not None:
            filename = os.path.join(cwd, filename)

        with open(filename, 'wb') as f:
            f.write(data)

        cls._run_bzr(['add', filename], cwd=cwd, *args, **kwargs)
        cls._run_bzr(['commit', '-m', msg, '--author', 'Test User'],
                     cwd=cwd, *args, **kwargs)

    def _compare_diffs(self, filename, full_diff, expected_diff_digest,
                       change_type='modified'):
        """Compare expected metadata to a generated diff.

        Args:
            filename (unicode):
                The expected filename in the diff.

            full_diff (bytes):
                The generated diff content.

            expected_diff_digest (bytes):
                The expected MD5 digest of the diff, past the headers
                (starting on the 3rd line).

            change_type (unicode, optional):
                The expected change type listed in the header.

        Raises:
            AssertionError:
                One of the expectations failed.
        """
        filename = filename.encode('utf-8')
        change_type = change_type.encode('utf-8')

        diff_lines = full_diff.splitlines()

        self.assertEqual(diff_lines[0],
                         b"=== %s file '%s'" % (change_type, filename))
        self.assertTrue(diff_lines[1].startswith(b'--- %s\t' % filename))
        self.assertTrue(diff_lines[2].startswith(b'+++ %s\t' % filename))

        diff_body = b'\n'.join(diff_lines[3:])
        self.assertEqual(md5(diff_body).hexdigest(), expected_diff_digest)

    def _count_files_in_diff(self, diff):
        return len([
            line
            for line in diff.split(b'\n')
            if line.startswith(b'===')
        ])

    def test_get_repository_info_original_branch(self):
        """Testing BazaarClient get_repository_info with original branch"""
        os.chdir(self.original_branch)
        ri = self.client.get_repository_info()

        self.assertTrue(isinstance(ri, RepositoryInfo))
        self.assertEqual(os.path.realpath(ri.path),
                         os.path.realpath(self.original_branch))

        self.assertEqual(ri.base_path, '/')

    def test_get_repository_info_child_branch(self):
        """Testing BazaarClient get_repository_info with child branch"""
        os.chdir(self.child_branch)
        ri = self.client.get_repository_info()

        self.assertTrue(isinstance(ri, RepositoryInfo))
        self.assertEqual(os.path.realpath(ri.path),
                         os.path.realpath(self.child_branch))

        self.assertEqual(ri.base_path, "/")

    def test_get_repository_info_no_branch(self):
        """Testing BazaarClient get_repository_info, no branch"""
        self.chdir_tmp()
        ri = self.client.get_repository_info()
        self.assertEqual(ri, None)

    def test_too_many_revisions(self):
        """Testing BazaarClient parse_revision_spec with too many revisions"""
        self.assertRaises(TooManyRevisionsError,
                          self.client.parse_revision_spec,
                          [1, 2, 3])

    def test_diff_simple(self):
        """Testing BazaarClient simple diff case"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'delete and modify stuff')

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs('foo.txt', result['diff'],
                            'a6326b53933f8b255a4b840485d8e210')

    def test_diff_exclude(self):
        """Testing BazaarClient diff with file exclusion"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        self._bzr_add_file_commit('exclude.txt', FOO2, 'commit 2')

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions, exclude_patterns=['exclude.txt'])
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs('foo.txt', result['diff'],
                            'a6326b53933f8b255a4b840485d8e210')

        self.assertEqual(self._count_files_in_diff(result['diff']), 1)

    def test_diff_exclude_in_subdir(self):
        """Testing BazaarClient diff with file exclusion in a subdirectory"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')

        os.mkdir('subdir')
        os.chdir('subdir')

        self._bzr_add_file_commit('exclude.txt', FOO2, 'commit 2')

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions,
                                  exclude_patterns=['exclude.txt', '.'])
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs('foo.txt', result['diff'],
                            'a6326b53933f8b255a4b840485d8e210')

        self.assertEqual(self._count_files_in_diff(result['diff']), 1)

    def test_diff_exclude_root_pattern_in_subdir(self):
        """Testing BazaarClient diff with file exclusion in the repo root"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('exclude.txt', FOO2, 'commit 1')

        os.mkdir('subdir')
        os.chdir('subdir')

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 2')

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(
            revisions,
            exclude_patterns=[os.path.sep + 'exclude.txt',
                              os.path.sep + 'subdir'])

        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs(os.path.join('subdir', 'foo.txt'), result['diff'],
                            '4deffcb296180fa166eddff2512bd0e4',
                            change_type='added')

    def test_diff_specific_files(self):
        """Testing BazaarClient diff with specific files"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'delete and modify stuff')
        self._bzr_add_file_commit('bar.txt', b'baz', 'added bar')

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions, ['foo.txt'])
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs('foo.txt', result['diff'],
                            'a6326b53933f8b255a4b840485d8e210')

    def test_diff_simple_multiple(self):
        """Testing BazaarClient simple diff with multiple commits case"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2')
        self._bzr_add_file_commit('foo.txt', FOO3, 'commit 3')

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs('foo.txt', result['diff'],
                            '4109cc082dce22288c2f1baca9b107b6')

    def test_diff_parent(self):
        """Testing BazaarClient diff with changes only in the parent branch"""
        self._bzr_add_file_commit('foo.txt', FOO1, 'delete and modify stuff',
                                  cwd=self.child_branch)

        grand_child_branch = make_tempdir()
        self._run_bzr(['branch', '--use-existing-dir', self.child_branch,
                       grand_child_branch],
                      cwd=self.child_branch)
        os.chdir(grand_child_branch)

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self.assertEqual(result['diff'], None)

    def test_diff_grand_parent(self):
        """Testing BazaarClient diff with changes between a 2nd level
        descendant"""
        self._bzr_add_file_commit('foo.txt', FOO1, 'delete and modify stuff',
                                  cwd=self.child_branch)

        grand_child_branch = make_tempdir()
        self._run_bzr(['branch', '--use-existing-dir', self.child_branch,
                       grand_child_branch],
                      cwd=self.child_branch)
        os.chdir(grand_child_branch)

        # Requesting the diff between the grand child branch and its grand
        # parent:
        self.options.parent_branch = self.original_branch

        revisions = self.client.parse_revision_spec([])
        result = self.client.diff(revisions)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('diff' in result)

        self._compare_diffs('foo.txt', result['diff'],
                            'a6326b53933f8b255a4b840485d8e210')

    def test_guessed_summary_and_description(self):
        """Testing BazaarClient guessing summary and description"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2')
        self._bzr_add_file_commit('foo.txt', FOO3, 'commit 3')

        self.options.guess_summary = True
        self.options.guess_description = True
        revisions = self.client.parse_revision_spec([])
        commit_message = self.client.get_commit_message(revisions)

        self.assertEqual('commit 3', commit_message['summary'])

        description = commit_message['description']
        self.assertTrue('commit 1' in description)
        self.assertTrue('commit 2' in description)
        self.assertFalse('commit 3' in description)

    def test_guessed_summary_and_description_in_grand_parent_branch(self):
        """Testing BazaarClient guessing summary and description for grand
        parent branch"""
        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1',
                                  cwd=self.child_branch)
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2',
                                  cwd=self.child_branch)
        self._bzr_add_file_commit('foo.txt', FOO3, 'commit 3',
                                  cwd=self.child_branch)

        self.options.guess_summary = True
        self.options.guess_description = True

        grand_child_branch = make_tempdir()
        self._run_bzr(['branch', '--use-existing-dir', self.child_branch,
                       grand_child_branch],
                      cwd=self.child_branch)
        os.chdir(grand_child_branch)

        # Requesting the diff between the grand child branch and its grand
        # parent:
        self.options.parent_branch = self.original_branch

        revisions = self.client.parse_revision_spec([])
        commit_message = self.client.get_commit_message(revisions)

        self.assertEqual('commit 3', commit_message['summary'])

        description = commit_message['description']
        self.assertTrue('commit 1' in description)
        self.assertTrue('commit 2' in description)
        self.assertFalse('commit 3' in description)

    def test_guessed_summary_and_description_with_revision_range(self):
        """Testing BazaarClient guessing summary and description with a
        revision range"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2')
        self._bzr_add_file_commit('foo.txt', FOO3, 'commit 3')

        self.options.guess_summary = True
        self.options.guess_description = True
        revisions = self.client.parse_revision_spec(['2..3'])
        commit_message = self.client.get_commit_message(revisions)

        self.assertEqual('commit 2', commit_message['summary'])
        self.assertEqual('commit 2', commit_message['description'])

    def test_parse_revision_spec_no_args(self):
        """Testing BazaarClient.parse_revision_spec with no specified
        revisions"""
        os.chdir(self.child_branch)

        base_commit_id = self.client._get_revno()
        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        tip_commit_id = self.client._get_revno()

        revisions = self.client.parse_revision_spec()
        self.assertTrue(isinstance(revisions, dict))
        self.assertTrue('base' in revisions)
        self.assertTrue('tip' in revisions)
        self.assertTrue('parent_base' not in revisions)
        self.assertEqual(revisions['base'], base_commit_id)
        self.assertEqual(revisions['tip'], tip_commit_id)

    def test_parse_revision_spec_one_arg(self):
        """Testing BazaarClient.parse_revision_spec with one specified
        revision"""
        os.chdir(self.child_branch)

        base_commit_id = self.client._get_revno()
        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        tip_commit_id = self.client._get_revno()

        revisions = self.client.parse_revision_spec([tip_commit_id])
        self.assertTrue(isinstance(revisions, dict))
        self.assertTrue('base' in revisions)
        self.assertTrue('tip' in revisions)
        self.assertTrue('parent_base' not in revisions)
        self.assertEqual(revisions['base'], base_commit_id)
        self.assertEqual(revisions['tip'], tip_commit_id)

    def test_parse_revision_spec_one_arg_parent(self):
        """Testing BazaarClient.parse_revision_spec with one specified
        revision and a parent diff"""
        os.chdir(self.original_branch)
        parent_base_commit_id = self.client._get_revno()

        grand_child_branch = make_tempdir()
        self._run_bzr(['branch', '--use-existing-dir', self.child_branch,
                       grand_child_branch])
        os.chdir(grand_child_branch)

        base_commit_id = self.client._get_revno()
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2')
        tip_commit_id = self.client._get_revno()

        self.options.parent_branch = self.child_branch

        revisions = self.client.parse_revision_spec([tip_commit_id])
        self.assertTrue(isinstance(revisions, dict))
        self.assertTrue('parent_base' in revisions)
        self.assertTrue('base' in revisions)
        self.assertTrue('tip' in revisions)
        self.assertEqual(revisions['parent_base'], parent_base_commit_id)
        self.assertEqual(revisions['base'], base_commit_id)
        self.assertEqual(revisions['tip'], tip_commit_id)

    def test_parse_revision_spec_one_arg_split(self):
        """Testing BazaarClient.parse_revision_spec with R1..R2 syntax"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        base_commit_id = self.client._get_revno()
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2')
        tip_commit_id = self.client._get_revno()

        revisions = self.client.parse_revision_spec(
            ['%s..%s' % (base_commit_id, tip_commit_id)])
        self.assertTrue(isinstance(revisions, dict))
        self.assertTrue('parent_base' not in revisions)
        self.assertTrue('base' in revisions)
        self.assertTrue('tip' in revisions)
        self.assertEqual(revisions['base'], base_commit_id)
        self.assertEqual(revisions['tip'], tip_commit_id)

    def test_parse_revision_spec_two_args(self):
        """Testing BazaarClient.parse_revision_spec with two revisions"""
        os.chdir(self.child_branch)

        self._bzr_add_file_commit('foo.txt', FOO1, 'commit 1')
        base_commit_id = self.client._get_revno()
        self._bzr_add_file_commit('foo.txt', FOO2, 'commit 2')
        tip_commit_id = self.client._get_revno()

        revisions = self.client.parse_revision_spec(
            [base_commit_id, tip_commit_id])
        self.assertTrue(isinstance(revisions, dict))
        self.assertTrue('parent_base' not in revisions)
        self.assertTrue('base' in revisions)
        self.assertTrue('tip' in revisions)
        self.assertEqual(revisions['base'], base_commit_id)
        self.assertEqual(revisions['tip'], tip_commit_id)
