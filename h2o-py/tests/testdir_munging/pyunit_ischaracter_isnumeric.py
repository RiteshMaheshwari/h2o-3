import sys
sys.path.insert(1, "../../")
import h2o
import random

def pyunit_ischaracter_isnumeric(ip,port):

    iris = h2o.import_file(h2o.locate("smalldata/iris/iris.csv"))
    assert iris[0].isnumeric(), "Expected the first column of iris to be numeric"
    assert not iris[0].ischaracter(), "Expected the first column of iris to be numeric"
    assert not iris[4].isnumeric(), "Expected the last column of iris to be character"
    iris[4] = iris[4].ascharacter()
    assert iris[4].isstring(), "Expected the last column of iris to be a string"

if __name__ == "__main__":
    h2o.run_test(sys.argv, pyunit_ischaracter_isnumeric)
