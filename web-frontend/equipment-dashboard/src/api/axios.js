import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
api.interceptors.response.use(
  res => res,
  async error => {
    if (error.response?.status === 401) {
      const refresh = localStorage.getItem("refresh");
      if (!refresh) throw error;

      const res = await axios.post(
        "http://127.0.0.1:8000/api/token/refresh/",
        { refresh }
      );

      localStorage.setItem("access", res.data.access);
      error.config.headers.Authorization = `Bearer ${res.data.access}`;
      return api(error.config);
    }
    throw error;
  }
);


export default api;
