import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        race_count = self.result["race_count"]

        self.assertEqual(race_count["White"], 27816)
        self.assertEqual(race_count["Black"], 3124)
        self.assertEqual(race_count["Asian-Pac-Islander"], 1039)
        self.assertEqual(race_count["Amer-Indian-Eskimo"], 311)
        self.assertEqual(race_count["Other"], 271)

    def test_average_age_men(self):
        self.assertEqual(
            self.result["average_age_men"],
            39.4
        )

    def test_percentage_bachelors(self):
        self.assertEqual(
            self.result["percentage_bachelors"],
            16.4
        )

    def test_higher_education_rich(self):
        self.assertEqual(
            self.result["higher_education_rich"],
            46.5
        )

    def test_lower_education_rich(self):
        self.assertEqual(
            self.result["lower_education_rich"],
            17.4
        )

    def test_min_work_hours(self):
        self.assertEqual(
            self.result["min_work_hours"],
            1
        )

    def test_rich_percentage(self):
        self.assertEqual(
            self.result["rich_percentage"],
            10.0
        )

    def test_highest_earning_country(self):
        self.assertEqual(
            self.result["highest_earning_country"],
            "Iran"
        )

    def test_highest_earning_country_percentage(self):
        self.assertEqual(
            self.result["highest_earning_country_percentage"],
            41.9
        )

    def test_top_india_occupation(self):
        self.assertEqual(
            self.result["top_IN_occupation"],
            "Prof-specialty"
        )


if __name__ == "__main__":
    unittest.main()