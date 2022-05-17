from nbresult import ChallengeResultTestCase
import numpy as np


class TestFeatureUnionCustomTransformers(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([[-1.224745, -1.224745, -1.224745, 0.166667],
                                [0., 0.,  0., 0.250],
                                [1.224745, 1.224745,  1.224745,  0.333333]])


        truth_test = np.array([[-1.224745, -1.224745, -1.224745, 0.166667],
                               [0., 0., 0., 0.250],
                               [1.224745,  1.224745,  7.348469,  0.333333]])

        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))
