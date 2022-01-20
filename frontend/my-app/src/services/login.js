import http from './http-common'

class UserDataService {
    loginUser(email, password) {
        return http.get(`/user/${email}/${password}`)
    }

}

export default new UserDataService();