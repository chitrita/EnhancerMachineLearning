import unittest
import random
import cbust_result

testfilepathf3 = "cbust_example/f3results.txt"
testfilepathf1 = "cbust_example/f1results.txt"
testfilepathjaspar = "cbust_example/jaspar2.txt"

class test_cbust_result(unittest.TestCase):

    def test_jaspar_instantiation_f3(self):
        self.newObj = cbust_result.cbust_result(testfilepathf3, "f3", testfilepathjaspar)
        self.assertIsInstance(self.newObj.jaspar_matrix_dict, dict)

    def test_identifier_set_f3(self):
        self.newObj = cbust_result.cbust_result(testfilepathf3,"f3", testfilepathjaspar)
        self.assertNotEqual(len(self.newObj._retrieve_reliable_motifs(0.4,0.05)), 0)

    def test_getter_for_reliable_motif_isdict_f3(self):
        self.newObj = cbust_result.cbust_result(testfilepathf3,"f3", testfilepathjaspar)
        self.assertIsInstance(self.newObj.calculate_reliable_motif_dict(0.4, 0.05), dict)

    def test_getter_for_reliable_motif_notempty_f3(self):
        self.newObj = cbust_result.cbust_result(testfilepathf3,"f3", testfilepathjaspar)
        self.assertNotEqual(len(self.newObj.calculate_reliable_motif_dict(0.4, 0.05)), 0)

    @unittest.skip
    def test_getter_for_reliable_motif_notempty_large_data_f3(self):
        self.large_object = cbust_result.cbust_result("CBUSToutput/CBUSToutput_I_vs_P_f3.txt","f3",
                                              "HomerOutput/HomerOutput-I_vs_P/homerMotifs.all.motifs")
        reliable_large_dict = self.large_object.calculate_reliable_motif_dict(0.4, 0.05)
        print(random.choice(list(reliable_large_dict.items())))
        self.assertNotEqual(len(reliable_large_dict), 0)

    def test_motif_matrix_writer_f3(self):
        self.newObj = cbust_result.cbust_result(testfilepathf3,"f3", testfilepathjaspar)
        reliable_dict = self.newObj.calculate_reliable_motif_dict(0.4, 0.05)
        self.newObj.write_reliable_motif_matrix(reliable_dict, "cbust_example/test_writer_matrix.txt")

    def test_instantiation_f1(self):
        self.newObj = cbust_result.cbust_result(testfilepathf1, "f1", testfilepathjaspar)
        self.assertIsInstance(self.newObj.f1_matrix_dict, dict)

    def test_instantiation_f1_big(self):
        self.newObj = cbust_result.cbust_result("immovable_data/Homer_Preg_TOTAL_cbustOut", "f1", None)
        self.assertIsInstance(self.newObj.f1_matrix_dict, dict)


if __name__ == '__main__':
    unittest.main()