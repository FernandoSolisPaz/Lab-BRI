export const getLogo = (pagina: string) => {
  const logos = {
    "PDI": "https://upload.wikimedia.org/wikipedia/commons/9/97/Polic%C3%ADa_de_Investigaciones_de_Chile_%28PDI%29_01.jpg",
    "Carabineros": "https://images.steamusercontent.com/ugc/2126318308534247985/D2B95F860D2D88AD6AC0A2C201CE4C25D61BCA73/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
    "Fiscalía": "https://pbs.twimg.com/profile_images/1807767458452803584/mVWy65iB_400x400.jpg",
    "ECOH": "https://santacruzfm.cl/wp-content/uploads/elementor/thumbs/WhatsApp-Image-2023-11-14-at-16.42.07-qq3ithcoq1l2lft14p0p7dr87v7qdqicxqgfngosyu.jpeg",
    "Radio Duna": "https://cdn-profiles.tunein.com/s25108/images/logog.jpg?t=155673",
    "El Dinamo": "https://www.eldinamo.cl/_templates/globals/img/logo.jpg",
    "Emol": "https://pbs.twimg.com/profile_images/816281345747980288/XtL97I6M_400x400.jpg",
    "Radio ADN": "https://p16-common-sign-va.tiktokcdn-us.com/tos-maliva-avt-0068/5da1a2716098c787c0f3878f26c461d0~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=205c0e40&x-expires=1752746400&x-signature=3VJHJPvvOOjcvt8Y2DnfA0XNsOc%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
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