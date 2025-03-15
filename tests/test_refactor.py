import glob
from hashlib import sha256
from pathlib import Path
import shutil
import sys
import tempfile

import pytest

# if root directory is not in sys.path, add it
root = str(Path(".").absolute())
if root not in sys.path:
    sys.path.append(root)
print(f"{sys.path = }")

ORIGINAL_HASH = "0f51b4fca41b7fd509e4b8f9d543151f68efa5e97b08493e4b2a0c06f5d8d5e2"


def find_original_rom() -> Path | None:
    """ `None` if not found """
    sfc_files = glob.glob("*.sfc")
    for sfc_file in sfc_files:
        path = Path(sfc_file)
        hash_ = sha256(path.read_bytes()).hexdigest()
        if hash_ == ORIGINAL_HASH:
            return path
    # no matching hash found
    return None


def compare_hash(flags: list[str], expected_hash: str) -> None:
    original_rom = find_original_rom()
    if not original_rom:
        assert False, "no original rom found"

    result_hash = None
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        temp_original_path = temp_dir_path / "ff6.sfc"
        shutil.copy(original_rom, temp_original_path)
        print(f"{temp_original_path = }")
        assert temp_original_path.exists()

        sys.argv = sys.argv[:1] + ["-i", str(temp_original_path)] + flags
        print(f"{sys.argv = }")
        if "args" in sys.modules:
            for mod_name, mod in list(sys.modules.items()):
                file = getattr(mod, "__file__", "")
                if file and "WorldsCollide" in file:
                    sys.modules.pop(mod_name)
        from WorldsCollide.wc import main
        main()

        dir_list = glob.glob(str(temp_dir_path) + "/*.sfc")
        assert len(dir_list) == 2, dir_list
        randomized_file = next(name for name in dir_list if not name.endswith("ff6.sfc"))
        randomized_file_path = Path(randomized_file)
        result_hash = sha256(randomized_file_path.read_bytes()).hexdigest()
    assert result_hash == expected_hash, f"{flags = } {result_hash = }"


params = [
    # (["-s", "1"], "0"),  # assert(item_possible) fails
    (["-s", "2"], "b06e39606144921d2f683e0db467698b3b9cc2f768c292c5111a5a26365c1a1f"),
    ([
        "-s", "12",
        "-fc",
        "-ir", "stronger", "-mca", "-stra", "-saw",
        "-scc", "-rec1", "7", "-rec2", "15", "-rec3", "16",
        "-sed", "-sfb", "-asr", "3.5",
        # I can't find anything that doesn't fail item_possible with these options:
        # "-ccrs",  # TODO: others in mutually exclusive group
        # "-chrm", "4", "6", "-cms",
        "-oa", "2.3.3.2.12.12.4.24.24.6.8.8",
        "-ob", "3.1.1.2.9.9.4.12.12.10.21.21",
        "-oc", "30.8.8.1.1.11.8",
        "-od", "59.1.1.11.31",
        "-ond", "-scan", "-warp",
        "-npctips",
        "-cg",
        "-ess", "-elrt", "-ebs", "-emps", "-eebr", "5", "-ems", "-emi",
        "-sirt", "-sprp", "80", "90", "-ssf8", "-npi", "-sebr", "-sesb",
        "-bbr", "-srp3", "-bnds", "-bnu",
        "-pd", "-nosaves", "-u254",
        "-res",
        "-sch", "-ssd", "2",
        "-cpor", "375.382.268.3.205.45.270.209.70.81.311.53.400.267.14",
        "-cspr", "267.8.92.3.56.207.315.321.341.313.90.325.308.85.307.70.138.6.156.73",
        "-cspp", "2.1.1.4.0.0.0.3.3.4.5.3.3.5.1.0.6.1.0.3",
        "-frw", "-wmhc", "-ahtc",
        "-ymain", "-etr",
    ], "e3f097222ff38da360e60aac2187014487d427439364f27f9a54dc82762d8589"),
    ([
        "-s", "17",
        "-cg",
        "-ir", "premium",
        "-ietr",
        "-com", "98989898989898989898989898",
        "-esrt", "-elr", "-stesp", "2", "4", "-ebr", "80", "-emprv", "10", "20", "-eer", "4", "6",
        "-yrandom", "-etn",
    ], "1f7d89c13c8ded9e190404814818524c390a7d462e86bafa60d69ce10f2982c6"),
    ([  # ultros league
        "-s", "19",
        "-cg",
        "-oa", "2.2.2.2.6.6.4.9.9", "-ob", "3.1.1.2.9.9.4.12.12.10.22.22",
        "-oc", "30.8.8.1.1.11.8", "-od", "59.1.1.11.31",
        "-sc1", "random", "-sc2", "random", "-sc3", "random",
        "-sal", "-eu", "-csrp", "80", "125",
        "-fst", "-brl", "-slr", "6", "10",
        "-lmprp", "75", "125",
        "-lel",
        "-srr", "25", "35",
        "-rnl", "-rnc", "-sdr", "1", "2",
        "-das", "-dda", "-dns", "-sch", "-scis",
        "-com", "98989898989898989898989898", "-rec1", "28", "-rec2", "27", "-xpm", "3", "-mpm", "5", "-gpm", "5",
        "-nxppd", "-lsced", "2", "-hmced", "2", "-xgced", "2", "-ase", "2", "-msl", "40", "-sed", "-bbs",
        "-drloc", "shuffle", "-stloc", "mix", "-be", "-bnu", "-res",
        "-fer", "0", "-escr", "100", "-dgne", "-wnz", "-mmnu", "-cmd",
        "-esr", "2", "5", "-elrt", "-ebr", "82", "-emprp", "75", "125",
        "-nm1", "random", "-rnl1", "-rns1", "-nm2", "random", "-rnl2", "-rns2",
        "-nmmi", "-mmprp", "75", "125", "-gp", "5000", "-smc", "3", "-sto", "1", "-ieor", "33", "-ieror", "33",
        "-ir", "stronger", "-csb", "7", "15", "-mca", "-stra", "-saw",
        "-sisr", "20", "-sprp", "75", "125", "-sdm", "5", "-npi", "-sebr", "-snsb", "-snee", "-snil", "-ccsr", "20",
        "-chrm", "0", "0", "-cms", "-frw", "-wmhc", "-cor", "100", "-crr", "100", "-crvr", "100", "120", "-crm",
        "-ari", "-anca", "-adeh", "-ame", "1", "-nmc", "-noshoes", "-u254", "-nfps",
        "-fs", "-fe", "-fvd", "-fr", "-fj", "-fbs", "-fedc", "-fc", "-ond", "-rr", "-etn",
    ], "3f514b916c4b269f0d8ce5363ae7b679518a80dae885a98b2975af00af075178"),
]


@pytest.mark.parametrize("flags, expected_hash", params)
def test_refactor(flags: list[str], expected_hash: str) -> None:
    compare_hash(flags, expected_hash)


if __name__ == "__main__":
    param_set = params[2]
    test_refactor(*param_set)
