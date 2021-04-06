from django.test import TestCase
from PDBParser.myPDBParser import PDBParser


def validate_pdb(file_name):
    try:
        parser = PDBParser(PERMISSIVE=0)
        structure_id = "inputFile"
        filename = file_name
        structure = parser.get_structure(structure_id, filename)

        return None
    except (Exception) as e:
        
        return e


class TestValidator(TestCase):

    # No errors
    def test_ValidPDB(self):

        self.assertEqual(True, validate_pdb('testPDBs/input1.pdb'))

    # Line partially Missing
    def test_NonValidPDB(self):

        self.assertEqual(False, validate_pdb('testPDBs/input2.pdb'))

    # Space mid line
    def test_ParsingErrorValidPDB(self):

        self.assertEqual(False, validate_pdb('testPDBs/input3.pdb'))

    # Space start of line
    def test_ParsingMidLineErrorPDB(self):

        self.assertEqual(True, validate_pdb('testPDBs/input4.pdb'))


def main():
    validate_pdb("input1.pdb")
    return 0


if __name__ == "__main__":
    main()
