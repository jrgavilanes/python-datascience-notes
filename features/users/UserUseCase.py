from features.users.UserRepository import UserRepository, UserModel, user_default_values


class UserUseCase:
    def __init__(self, user_repository: UserRepository = None):
        if not user_repository:
            raise Exception(str("No repository given"))

        self.userRepository = user_repository

    def get_next_id(self) -> int:
        return self.userRepository.get_next_id()

    def get_by_id(self, record_id: int) -> dict:
        return self.userRepository.get_by_id(record_id=record_id)

    def get_all_records(self) -> dict:
        return self.userRepository.get_all_records()

    def upsert(self, user_data: dict, request_method: str) -> UserModel:

        user = {field: user_data.get(field, default) for field, default in user_default_values().items()}

        if user["id"] is None and request_method == "POST":
            user["id"] = self.userRepository.get_next_id()

        new_user = UserModel(user_id=user["id"],
                             name=user["name"],
                             email=user["email"],
                             password=user["password"],
                             country=user["country"]
                             )

        self.userRepository.upsert(new_user)

        return new_user

    def delete_by_id(self, record_id: int) -> int:
        return self.userRepository.delete_by_id(record_id=record_id)

    def commit(self, csv_file=None, sep=None) -> (bool, str):
        return self.userRepository.commit(csv_file=csv_file, sep=sep)
