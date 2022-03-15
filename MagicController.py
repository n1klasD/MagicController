import time
from abc import ABC

# from Configuration import ConfigurationHandler
from util import User
from Communication import CommunicationHandler
from FaceRecognition import FaceAuthentication
from FaceRecognition import MirrorFaceOutput
from Configuration import ConfigurationHandler


class Mediator(ABC):
    def notify(self, sender: object, *args) -> None:
        pass


class BaseComponent:

    def __init__(self, mediator: Mediator = None):
        self.mediator = mediator


class MagicController(Mediator):
    def __init__(self):
        self.communication_handler = CommunicationHandler(self)
        self.face_authentication = FaceAuthentication(benchmark_mode=True, lite=True, resolution=(640, 480), mediator=self)

    '''
        self._currentUser = User()
        self._configurationHandler = ConfigurationHandler()
        self.userDetected(self._currentUser)

    def getCurrentUser(self) -> User:
        """
        Gets user which is currently logged on. This might also be the default user.

        Returns:
            User: The user which is logged onto the mirror.
        """

        return self._currentUser

    def userDetected(self, detectedUser: User):
        """
        This method is called by the face recognition if a user is detected. It prompts the ConfigurationHandler to
        update the config file

        Args:
            detectedUser (User): The user which was detected by the camera

        Returns:

        """

        if detectedUser.getIdentifier() != self._currentUser.getIdentifier():
            self._configurationHandler.updateConfiguration(detectedUser)

            self._currentUser = detectedUser

            # TODO: Notify the CommunicationHandler to tell the module to refresh

    '''

    def notify(self, sender: object, *args) -> None:
        # communicationhandler sends request to register a user
        if isinstance(sender, CommunicationHandler.CreateUser):
            callback = args[0]
            user_id = args[1]
            images = args[2]

            # Call FaceAuthentication to register faces
            success = self.face_authentication.register_faces(1, images, min_number_faces=1, mode='fast')

            # call callback, to send the response to the http server.
            callback(success)

        # Face Recognition detected a face
        if isinstance(sender, MirrorFaceOutput):
            detected_user_id = args[0]

            if detected_user_id is None:
                ConfigurationHandler.updateConfiguration(0)
            else:
                ConfigurationHandler.updateConfiguration(detected_user_id)

            self.trigger_refresh()

    def trigger_refresh(self):
        print("Mirror Refresh")


def main():
    MagicController()


if __name__ == '__main__':
    main()
