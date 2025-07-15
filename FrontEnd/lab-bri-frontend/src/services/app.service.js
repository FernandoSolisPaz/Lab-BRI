import httpClient from "../http-common"


const listarComunas = () => {
    return httpClient.get(`/buscar/comunas`);
}

const obtenerComuna = (nombre) => {
    return httpClient.get(`/buscar/obtenerComuna?nombre=${nombre}`);
}

const buscarDocumento= (data) => {
    return httpClient.post(`/buscar`, data);
}

export default {obtenerComuna, listarComunas, buscarDocumento};