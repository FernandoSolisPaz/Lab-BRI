import axios from "axios";

// Crea una instancia de Axios
const httpClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // Cambia esto por la URL de tu backend
  // baseURL: "http://localhost:8081", // Cambia esto por la URL de tu backend
  headers: {
    "Content-type": "application/json",
  },
});

export default httpClient;