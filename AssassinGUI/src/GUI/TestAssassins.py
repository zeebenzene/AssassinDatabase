import unittest
import os
import os.path
from AssassinSearch import Search

class Test(unittest.TestCase):


    def setUp(self):
        self.sch = Search()
        self.fullDict = {"name" : "booboo", 
               "minAge" : 0,
               "maxAge" : 50,
               "minHeight" : 0,
               "maxHeight" : 500,
               "minWeight" : 100,
               "maxWeight" : 250,
               "nationality" : "Chinese",
               "employer" : "KGB",
               "avgRating" : 3,
               "successes" : 85,
               "minMission" : 5,
               "maxMission" : 500,
               "SmissionMin" : 10,
               "SmissionMax" : 490}
        self.emptyDict = {"name" : "name", 
                          "minAge" : "min",
                          "maxAge" : "max",
                          "minHeight" : "min(cm)",
                          "maxHeight" : "max(cm)",
                          "minWeight" : "min(lbs)",
                          "maxWeight" : "max(lbs)",
                          "nationality" : "select one",
                          "employer" : "select one",
                          "avgRating" : "select one",
                          "successes" : "min(%)",
                          "minMission" : "min",
                          "maxMission" : "max",
                          "SmissionMin" : "min",
                          "SmissionMax" : "max"}
        
    def test_full(self):
        actualQuery = self.sch.getQuery(self.fullDict)
        expectedQuery = "SELECT AMBasicInfo.id FROM AMBasicInfo JOIN AMEmployment ON AMEmployment.id = AMBasicInfo.id JOIN AMFlavor ON AMFlavor.id = AMEmployment.id JOIN AMReviews ON AMReviews.id = AMFlavor.id JOIN AMImages ON AMFlavor.id = AMImages.id WHERE  AMBasicInfo.name = \"booboo\" AND AMBasicInfo.age >= 0 AND AMBasicInfo.age <= 50 AND AMBasicInfo.weight >= 100 AND AMBasicInfo.weight <= 250 AND AMBasicInfo.height >= 0 AND AMBasicInfo.height <= 500 AND AMBasicInfo.nationality = \"Chinese\" AND AMEmployment.past_employers = \"KGB\" AND AMEmployment.num_jobs >= 5 AND AMEmployment.num_jobs <= 500 AND AMEmployment.num_successful >= 10 AND AMEmployment.num_successful <= 490 AND AMEmployment.average_successes >= 85 AND AMReviews.current_average >=3 GROUP BY AMBasicInfo.id"
        self.assertEqual(actualQuery, expectedQuery )
    
    def test_empty(self):
        actualQuery = self.sch.getQuery(self.emptyDict)
        print(actualQuery)
        expectedQuery = "SELECT AMBasicInfo.id FROM AMBasicInfo JOIN AMEmployment ON AMEmployment.id = AMBasicInfo.id JOIN AMFlavor ON AMFlavor.id = AMEmployment.id JOIN AMReviews ON AMReviews.id = AMFlavor.id JOIN AMImages ON AMFlavor.id = AMImages.id GROUP BY AMBasicInfo.id"

        self.assertEqual(actualQuery, expectedQuery)    
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()