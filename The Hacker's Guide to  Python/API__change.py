import warnings

class Car(object):

    def turn_left(self):
        '''
        turn the car left.
        deprecated:: 1.1
            Use: func: 'turn' instead with the direction argument set to left.
        :return:
        '''
        warnings.warn('turn_left is deprecated, user turn instead.',
                      DeprecationWarning)
        self.turn(direction='left')
    def turn(self, direction):
        '''
        Turn the car in some direction.


        :param direction: the direction to turn to .
        : type direction: str
        :return:
        '''
        pass


print Car().turn_left()
