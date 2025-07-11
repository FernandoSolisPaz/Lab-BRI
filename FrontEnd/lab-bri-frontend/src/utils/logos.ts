export const getLogo = (pagina: string) => {
  const logos = {
    "BioBio Chile": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxaKtXVa_5rXYa3Jv-L65j6h9xNofU4oeTkw&s",
    "CNN Chile": "https://upload.wikimedia.org/wikipedia/commons/0/04/Logo_cnnchile.png",
    "La Tercera": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzn9W65Z27kiAcLB-2YZysqTSS_EDoqvCtng&s",
    "CHV Noticias": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Logo_CHV_2015.png",
    "Mega Noticias": "https://static-cdn.jtvnw.net/jtv_user_pictures/6c5d6466-2ab2-4bf7-9e4d-79b156e08823-profile_image-300x300.png",
    "Radio Cooperativa": "https://app.cooperativa.cl/apps/site/artic/20220718/imag/foto_0000001220220718133642.png",
    "T13": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Logotipo_de_Teletrece.svg/1200px-Logotipo_de_Teletrece.svg.png",
  }
  return logos[pagina as keyof typeof logos] || "https://i.pinimg.com/1200x/7b/71/35/7b7135945421f5d2a7e3b11830f8f227.jpg"
}