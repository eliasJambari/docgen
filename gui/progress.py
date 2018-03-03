import logging
logger = logging.getLogger()

n_tasks = 0
progression = 0


def tmp_solution(weight, step, debug = None):
    global progression
    progression += weight

    print(str(progression/n_tasks*100) + " % - " + step)

    if debug is not None:
        logger.debug(debug)