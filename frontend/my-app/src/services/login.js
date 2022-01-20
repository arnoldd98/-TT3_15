import http from './http-common'

class UserDataService {
    loginUser(email, password) {
        return http.get(`/user/${email}/${password}`)
    }

}

export default new UserDataService();

// getAll(page = 0) {
//     return http.get(`?page=${page}`);
// }

// get(id) {
//     return http.get(`/id/${id}`);
// }

// find(query, by = "name", page = 0) {
//     return http.get(`?${by}=${query}&page=${page}`);
// }

// createReview(data) {
//     return http.post("/review", data);
// }

// updateReview(data) {
//     return http.put("/review", data);
// }

// deleteReview(id, userId) {
//     return http.delete(`/review?id=${id}`, {data:{user_id: userId}});
// }

// getCuisines(id) {
//     return http.get(`/cuisines`);
// }