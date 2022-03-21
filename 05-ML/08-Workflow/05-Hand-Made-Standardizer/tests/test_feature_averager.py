from nbresult import ChallengeResultTestCase
import numpy as np


class TestFeatureAverager(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([[0.166667], [0.250000], [0.333333]])

        truth_test = np.array([[0.166667], [0.250000], [0.333333]])

        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))
