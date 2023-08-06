from zoofs.baseoptimizationalgorithm import BaseOptimizationAlgorithm
import numpy as np
import time
import warnings


class DragonFlyOptimization(BaseOptimizationAlgorithm):
    def __init__(
        self,
        objective_function,
        n_iteration: int = 1000,
        timeout: int = None,
        population_size=50,
        method="sinusoidal",
        minimize=True,
        logger=None,
        **kwargs,
    ):
        """
        Parameters
        ----------
        objective_function: user made function of the signature 'func(model,X_train,y_train,X_test,y_test)'
            User defined function that returns the objective value

        population_size: int, default=50
            Total size of the population

        n_iteration: int, default=1000
            Number of time the Optimization algorithm will run

        timeout: int = None
            Stop operation after the given number of second(s).
            If argument is set to None, the operation is executed without time limitation and n_iteration is followed

        method : {'linear','random','quadraic','sinusoidal'}, default='sinusoidal'
            Choose the between the three methods of Dragon Fly optimization

        minimize : bool, default=True
            Defines if the objective value is to be maximized or minimized

        logger: Logger or None, optional (default=None)
            - accepts `logging.Logger` instance.

        **kwargs
            Any extra keyword argument for objective_function

        Attributes
        ----------
        best_feature_list : ndarray of shape (n_features)
            list of features with the best result of the entire run
        """
        super().__init__(
            objective_function, n_iteration, timeout, population_size, minimize, logger, **kwargs
        )
        self.method = method

    def _evaluate_fitness(
        self, model, x_train, y_train, x_valid, y_valid, particle_swarm_flag=0, dragon_fly_flag=0
    ):
        return super()._evaluate_fitness(
            model, x_train, y_train, x_valid, y_valid, particle_swarm_flag, dragon_fly_flag
        )

    def _check_params(self, model, x_train, y_train, x_valid, y_valid, method):
        super()._check_params(model, x_train, y_train, x_valid, y_valid)
        if method not in ["linear", "random", "quadraic", "sinusoidal"]:
            raise ValueError("method accepts only linear,random,quadraic types ")

    def fit(self, model, X_train, y_train, X_valid, y_valid, verbose=True):
        """
        Parameters
        ----------
        model : machine learning model's object
           machine learning model's object

        X_train : pandas.core.frame.DataFrame of shape (n_samples, n_features)
           Training input samples to be used for machine learning model

        y_train : pandas.core.frame.DataFrame or pandas.core.series.Series of shape (n_samples)
           The target values (class labels in classification, real numbers in regression).

        X_valid : pandas.core.frame.DataFrame of shape (n_samples, n_features)
           Validation input samples

        y_valid : pandas.core.frame.DataFrame or pandas.core.series.Series of shape (n_samples)
            The target values (class labels in classification, real numbers in regression).

        verbose : bool,default=True
             Print results for iterations

        """
        self._check_params(model, X_train, y_train, X_valid, y_valid, self.method)

        self.feature_score_hash = {}
        kbest = self.population_size - 1
        self.feature_list = np.array(list(X_train.columns))
        self.best_results_per_iteration = {}
        self.best_score = np.inf
        self.worst_score = -np.inf
        self.worst_dim = np.ones(X_train.shape[1])
        self.best_dim = np.ones(X_train.shape[1])

        self.best_score_dimension = np.ones(X_train.shape[1])
        delta_x = np.random.randint(0, 2, size=(self.population_size, X_train.shape[1]))

        self.initialize_population(X_train)

        if self.timeout is not None:
            timeout_upper_limit = time.time() + self.timeout
        else:
            timeout_upper_limit = time.time()
        for i in range(self.n_iteration):

            if (self.timeout is not None) & (time.time() > timeout_upper_limit):
                warnings.warn("Timeout occured")
                break
            self._check_individuals()

            self.fitness_scores = self._evaluate_fitness(
                model, X_train, y_train, X_valid, y_valid, 0, 1
            )

            self.iteration_objective_score_monitor(i)

            if self.method == "linear":
                s = 0.2 - (0.2 * ((i + 1) / self.n_iteration))
                e = 0.1 - (0.1 * ((i + 1) / self.n_iteration))
                a = 0.0 + (0.2 * ((i + 1) / self.n_iteration))
                c = 0.0 + (0.2 * ((i + 1) / self.n_iteration))
                f = 0.0 + (2 * ((i + 1) / self.n_iteration))
                w = 0.9 - (i + 1) * (0.5) / (self.n_iteration)

            if self.method == "random":
                if 2 * (i + 1) <= self.n_iteration:
                    pct = 0.1 - (0.2 * (i + 1) / self.n_iteration)
                else:
                    pct = 0
                w = 0.9 - (i + 1) * (0.5) / (self.n_iteration)
                s = 2 * np.random.random() * pct
                a = 2 * np.random.random() * pct
                c = 2 * np.random.random() * pct
                f = 2 * np.random.random()
                e = pct

            if self.method == "quadraic":
                w = 0.9 - (i + 1) * (0.5) / (self.n_iteration)
                s = 0.2 - (0.2 * ((i + 1) / self.n_iteration)) ** 2
                e = 0.1 - (0.1 * ((i + 1) / self.n_iteration)) ** 2
                a = 0.0 + (0.2 * ((i + 1) / self.n_iteration)) ** 2
                c = 0.0 + (0.2 * ((i + 1) / self.n_iteration)) ** 2
                f = 0.0 + (2 * (i + 1) / self.n_iteration) ** 2

            if self.method == "sinusoidal":
                beta = 0.5
                w = 0.9 - (i + 1) * (0.5) / (self.n_iteration)
                s = 0.10 + 0.10 * np.abs(
                    np.cos(((i + 1) / self.n_iteration) * (4 * np.pi - beta * np.pi))
                )
                e = 0.05 + 0.05 * np.abs(
                    np.cos(((i + 1) / self.n_iteration) * (4 * np.pi - beta * np.pi))
                )
                a = 0.10 - 0.05 * np.abs(
                    np.cos(((i + 1) / self.n_iteration) * (4 * np.pi - beta * np.pi))
                )
                c = 0.10 - 0.05 * np.abs(
                    np.cos(((i + 1) / self.n_iteration) * (4 * np.pi - beta * np.pi))
                )
                f = 2 - 1 * np.abs(
                    np.cos(((i + 1) / self.n_iteration) * (4 * np.pi - beta * np.pi))
                )

            temp = individuals = self.individuals
            temp_2 = (
                temp.reshape(temp.shape[0], 1, temp.shape[1])
                - temp.reshape(1, temp.shape[0], temp.shape[1])
            ).reshape(temp.shape[0] ** 2, temp.shape[1]) ** 2
            temp_3 = temp_2.reshape(temp.shape[0], temp.shape[0], temp.shape[1]).sum(axis=2)
            zz = np.argsort(temp_3)
            cc = [list(iter1[iter1 != iter2]) for iter1, iter2 in zip(zz, np.arange(temp.shape[0]))]

            si = -(
                np.repeat(individuals, kbest, axis=0).reshape(
                    individuals.shape[0], kbest, individuals.shape[1]
                )
                - individuals[np.array(cc)[:, :kbest]]
            ).sum(axis=1)
            ai = delta_x[np.array(cc)[:, :kbest]].sum(axis=1) / kbest
            ci = (individuals[np.array(cc)[:, :kbest]].sum(axis=1) / kbest) - individuals
            fi = self.best_score_dimension - self.individuals
            ei = self.individuals + self.worst_dim

            delta_x = s * si + a * ai + c * ci + f * fi + e * ei + w * delta_x
            delta_x = np.where(delta_x > 6, 6, delta_x)
            delta_x = np.where(delta_x < -6, -6, delta_x)
            T = abs(delta_x / np.sqrt(1 + delta_x ** 2))
            self.individuals = np.where(
                np.random.uniform(size=(self.population_size, X_train.shape[1])) < T,
                np.logical_not(self.individuals).astype(int),
                individuals,
            )

            self.verbose_results(verbose, i)
            self.best_feature_list = list(self.feature_list[np.where(self.best_dim)[0]])
        return self.best_feature_list
