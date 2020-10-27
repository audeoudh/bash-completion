import pytest
import pwd


class TestFscrypt:
    @pytest.mark.complete("fscrypt -")
    def test_general_opts(self, completion):
        assert completion

    @pytest.mark.complete("fscrypt ")
    def test_commands(self, completion):
        assert set(completion) == {
            "--help", "--version",
            "encrypt", "lock", "metadata", "purge", "setup", "status", "unlock"
        }

    @pytest.mark.complete("fscrypt metadata ")
    def test_metadata(self, completion):
        assert set(completion) == {
            "--help", "--verbose", "--quiet",
            "add-protector-to-policy", "destroy", "change-passphrase",
            "dump", "remove-protector-from-policy", "create"
        }

    @pytest.mark.complete("fscrypt encrypt --user=")
    def test_user(self, completion):
        system_users = {p.pw_name for p in pwd.getpwall()}
        assert all((user in system_users) for user in completion)

    @pytest.mark.complete("fscrypt lock --drop-caches=")
    def test_drop_caches(self, completion):
        assert "false" in completion

    @pytest.mark.complete("fscrypt status -")
    def test_global_opts(self, completion):
        assert "--quiet" in completion \
                and "--verbose" in completion \
                and "--help" in completion

    @pytest.mark.complete("fscrypt metadata create ")
    def test_metadata_create(self, completion):
        assert set(completion) == {"policy", "protector"}
