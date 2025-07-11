<template>
    <v-container fluid class="pa-0 ma-0 fill-height">
        <v-row no-gutters class="fill-height">

            <!-- Columna izquierda: Lista de noticias -->
            <v-col cols="12" md="3" class="pa-2 fill-height">
                <v-card class="d-flex flex-column" height="100%">
                    <v-card-title class="text-h6 font-weight-bold">
                        Noticias
                    </v-card-title>
                    <v-divider></v-divider>

                    <!-- Scroll solo aquí -->
                    <v-card-text class="scrollable-news">
                        <div v-for="(noticia, index) in noticias" :key="index" class="mb-4 d-flex">
                            <!-- Logo -->
                            <v-img :src="getLogo(noticia.pagina)" width="60" height="60" class="mr-3 rounded" cover />
                            <!-- Contenido -->
                            <div class="flex-grow-1">
                                <div class="text-subtitle-1 font-weight-bold mb-1">
                                    {{ noticia.titulo.slice(0, 55) }}...
                                </div>
                                <div class="text-body-2">
                                    {{ noticia.texto.slice(0, 200) }}...
                                </div>
                                <div class="d-flex justify-end my-3">
                                    <v-btn color="red" variant="elevated" size="small" :href="noticia.hipervinculo"
                                        target="_blank">
                                        Ver más
                                    </v-btn>
                                </div>
                                <v-divider></v-divider>
                            </div>
                        </div>
                    </v-card-text>
                </v-card>
            </v-col>

            <!-- Columna derecha: MAPA -->
            <v-col cols="12" md="9" class="pa-2 fill-height">
                <Map ref="map" />
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
import Map from '../components/Map.vue'

export default {
    components: {
        Map
    },

    data() {
        return {
            noticias: [
                {
                    titulo: "Asaltan a hombre en Cerro Navia: le robaron $2 millones en productos y lo balearon antes de huir",
                    fecha_extraccion: "2025-06-20 15:34:00",
                    fecha_publicacion: "2025-01-25 12:26:00",
                    keywords: [
                        "delito",
                        "asalto a mano armada",
                        "robo"
                    ],
                    pagina: "BioBio Chile",
                    hipervinculo: "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/01/24/asaltan-a-hombre-en-cerro-navia-le-robaron-2-millones-en-productos-y-lo-balearon-antes-de-huir.shtml",
                    texto: "Carabineros investiga un asalto al dueño de un furgón en Cerro Navia. La víctima resultó baleada, sufrió lesiones graves, pero está fuera de riesgo vital.\nEl hecho ocurrió en la intersección de las calles La Lenga con El Raulí.\nMientras el conductor entregaba productos de cosmética, al menos tres desconocidos en un vehículo lo interceptaron, cerrándole el paso. Dos de ellos descendieron y robaron la totalidad de los productos que transportaba.\nAl huir, los asaltantes dispararon al menos dos veces desde el vehículo, luego de que la víctima intentara resistirse al robo. Uno de los disparos impactó en el furgón, mientras que el otro alcanzó la rodilla izquierda del conductor.\nLa víctima fue trasladada al Hospital Félix Bulnes con una lesión grave, aunque está fuera de riesgo vital.\nDiligencias de Carabineros tras el asalto en Cerro Navia\nEl mayor de Carabineros, Rodrigo Inzunza, detalló que el suceso ocurrió alrededor de las 10:00 horas de esta mañana.\n“Podría haber existido algún tipo de seguimiento. No obstante, todo es materia de investigación”, expresó el mayor Inzunza.\nAdemás, señaló que los delincuentes robaron 36 cajas de productos, valoradas en aproximadamente $2 millones.\nLa SIP de Carabineros investiga el caso y busca localizar el vehículo usado por los delincuentes, así como identificar a los responsables. No se descarta que Labocar participe en las diligencias, pues aún se espera la instrucción del Ministerio Público.",
                    autores: [
                        "Rodrigo Pino"
                    ],
                    ubicacion: "Cerro Navia",
                    imagen: "https://media.biobiochile.cl/wp-content/uploads/2025/01/social-asalto-cerro-navia-disparos-hombre-baleado.png"
                },
                {
                    titulo: "Con bomba molotov atacan micro en Cerro Navia",
                    fecha_extraccion: "2025-06-20 15:38:00",
                    fecha_publicacion: "2025-05-23 09:00:00",
                    keywords: [
                        "desorden público"
                    ],
                    pagina: "Radio Duna",
                    hipervinculo: "https://www.duna.cl/noticias/2025/05/23/con-bomba-molotov-atacan-micro-en-cerro-navia/",
                    texto: "Durante la noche de este jueves, un grupo de personas, realizó una serie de desmanes y delitos en Cerro Navia, terminando con la quema de un bus Red del transporte público.\nFue en la intercepción de la calle Santos Luis Medel con Avenida Mapocho, en que las personas abordaron el vehículo y le robaron el celular al conductor para después quemar el bus y darse a la fuga.\nPese a ello, el Ministerio Público dio cuenta de que un menor de edad de 17 años fue detenido por verse implicado en dicho delito.\nDe acuerdo a la información de Carabineros, los implicados en el hecho delictual habrían utilizado bombas molotov para incendiar el vehículo que, al momento del delito, se encontraba si pasajeros.\nAsí también, dieron a conocer que pese a la violencia situación, el conductor del bus no fue agredido físicamente y se encuentra en un buen estado de salud.",
                    autores: [
                        "Israel Durán Bustamante"
                    ],
                    ubicacion: "Cerro Navia",
                    imagen: "https://www.duna.cl/media/2025/05/A_UNO_1266251.jpg"
                },
                {
                    titulo: "Tres detenidos deja tiroteo en Cerro Navia: sujetos lanzaron sus armas durante la persecución",
                    fecha_extraccion: "2025-06-20 15:38:00",
                    fecha_publicacion: "2025-06-14 03:07:00",
                    keywords: [
                        "delito",
                        "tiroteo"
                    ],
                    pagina: "T13",
                    hipervinculo: "https://www.t13.cl/noticia/nacional/tres-detenidos-deja-tiroteo-cerro-navia-sujetos-lanzaron-sus-armas-durante-pers-14-6-2025",
                    texto: "Los detenidos, tres hombres chilenos de entre 20 y 30 años, fueron capturados luego de una acción coordinada entre diversos medios de Carabineros.\nUn intenso operativo policial culminó con la detención de tres hombres en la comuna de Cerro Navia, región Metropolitana, luego de una persecución que se desató tras una serie de disparos injustificados, según reportó el Teniente Mauricio Serrano, oficial de Ronda de la Prefectura Santiago Occidente.\nLos detenidos, tres hombres chilenos de entre 20 y 30 años, fueron capturados luego de una acción coordinada entre diversos medios de Carabineros, incluyendo unidades aéreas y vehículos de distintas comunas cercanas.\nSegún el teniente Serrano, yodo comenzó cuando Carabineros recibió una alerta a través de la línea 133 sobre un disparo injustificado realizado por un grupo de individuos. Al percatarse de la presencia policial en el lugar, los sujetos intentaron huir en un vehículo, lo que provocó un seguimiento articulado por varias unidades de carabineros. Durante la fuga, los individuos arrojaron diversos objetos desde el interior del vehículo, lo que generó más tensiones en el operativo.\nLa persecución terminó con la captura de los tres hombres, quienes fueron detenidos sin que se registraran heridos ni en la policía ni en los sospechosos. De acuerdo con Serrano, uno de los detenidos cuenta con antecedentes penales previos. “El procedimiento fue limpio y ajustado a derecho, sin que se hiciera uso de armas de fuego por parte de Carabineros”, comentó el Teniente.\nDurante el seguimiento, los individuos arrojaron desde el interior del vehículo armas de fuego, entre ellas una pistola marca Beretta calibre 9 mm. Al llegar al sitio del suceso, Carabineros encontró una importante cantidad de material balístico, con alrededor de 20 a 25 disparos de diferentes calibres y cartuchos de escopeta, lo que respalda la denuncia de una balacera en la zona.\nEl motivo de los disparos sigue siendo materia de investigación. La fiscalía se encuentra recabando pruebas, incluyendo el levantamiento de cámaras de seguridad, para determinar si los disparos fueron dirigidos al aire o a algún inmueble cercano. Además, se está evaluando el rol que jugaron los detenidos en el incidente, mientras se espera la instrucción de la fiscalía para proceder con el levantamiento de más pruebas.",
                    autores: [
                        "T13"
                    ],
                    ubicacion: "Cerro Navia",
                    imagen: "https://s.t13.cl/sites/default/files/styles/manualcrop_1600x800/public/t13/field-imagen/2025-06/Captura%20de%20pantalla%202025-06-14%20030043.png.jpeg?itok=7q_Yqq4l"
                },
                {
                    titulo: "Balacera en Cerro Navia dejó una persona fallecida y dos heridas",
                    fecha_extraccion: "2025-06-20 15:38:00",
                    fecha_publicacion: "2025-01-08 10:51:00",
                    keywords: [
                        "delito",
                        "tiroteo",
                        "fallecido",
                        "herido"
                    ],
                    pagina: "Radio Cooperativa",
                    hipervinculo: "https://cooperativa.cl/noticias/pais/policial/balacera-en-cerro-navia-dejo-una-persona-fallecida-y-dos-heridas/2025-01-08/103220.html",
                    texto: "Familiares de las víctimas llegaron al Hospital Félix Bulnes y amenazaron al personal médico, generando un nuevo foco de tensión.\nDos personas que se encontraban en el lugar fueron detenidas, pero se desconoce si están vinculadas al ataque.\nCerro Navia fue escenario de una violenta balacera la mañana de este miércoles en el sector de Conde de la Conquista, donde desconocidos dispararon desde un vehículo hacia una vivienda, donde dos mujeres y un hombre resultaron heridos.\nSin embargo, en el Hospital Félix Bulnes se confirmó el deceso de una de las mujeres, de 55 años, mientras que los heridos permanecen en riesgo vital.\nTestigos relataron que, antes del ataque, presenciaron a dos personas \"jóvenes y altas\" preparando armas largas y cortas, quienes posteriormente se trasladaron hasta el mencionado domicilio y, desde el exterior, efectuaron una cantidad indeterminada de disparos.\nEl incidente, que ocurrió cerca de las 07:30, movilizó a personal de Carabineros, quienes actualmente realizan peritajes en el lugar, recogiendo gran cantidad de evidencia balística. Los vecinos reportan que no es la primera vez que este punto, señalado como un presunto centro de venta de drogas, es escenario de disparos y desórdenes.\n\"Se recibió un comunicado a Carabineros respecto de la existencia de una persona fallecida y dos lesionadas en Cerro Navia. Las lesiones y el fallecimiento de esta persona -producto de armas de fuego- que se habrían producido en el exterior de un domicilio de la comuna\", informó Rossana Folli, fiscal ECOH (Equipo de Crimen Organizado y Homicidios).\n\"Por lo tanto, se dio aviso a la Fiscalía ECOH, quienes instruimos el trabajo de la Brigada de Homicidios (BH) de la PDI en el lugar\", agregó la persecutora.\nCarabineros detuvo a dos personas que se encontraban en un domicilio ubicado al costado de la balacera, aunque se desconoce -de momento- si están vinculadas con el ataque.\nEl hospital también vivió momentos de tensión cuando familiares de las víctimas llegaron a amenazar al personal médico, lo que obligó a reforzar la presencia policial en el recinto.\nResidentes del sector expresaron su preocupación, indicando que durante las festividades de Navidad y Año Nuevo ya se habían producido balaceras en la misma zona. Afirman estar atemorizados y cansados de la violencia que afecta al barrio, ubicado a pocas cuadras de la municipalidad de Cerro Navia.",
                    autores: [
                        "Cooperativa.cl"
                    ],
                    ubicacion: "Cerro Navia",
                    imagen: "https://cooperativa.cl/noticias/site/artic/20250108/imag/foto_0000000920250108103220.jpg"
                },
                {
                    titulo: "Mujer sufre violento robo en Cerro Navia: delincuentes la golpearon y huyeron con su vehículo",
                    fecha_extraccion: "2025-06-20 15:38:00",
                    fecha_publicacion: "2023-09-28 08:04:00",
                    keywords: [
                        "delito",
                        "robo",
                        "herido"
                    ],
                    pagina: "BioBio Chile",
                    hipervinculo: "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2023/09/28/mujer-sufre-violento-robo-en-cerro-navia-delincuentes-la-golpearon-y-huyeron-con-su-vehiculo.shtml",
                    texto: "Una mujer fue víctima de un violento robo en su domicilio de Cerro Navia, donde delincuentes huyeron con su vehículo.\nLa situación ocurrió anoche en Comandante Chacón.\nHasta un domicilio de dicha calle llegaron dos individuos a rostro cubierto, quienes fracturaron la puerta y enfrentaron a la única moradora que había en ese momento.Tras golpearla y lanzarla al suelo, le exigieron a la mujer la entrega de especies de valor. Ella les dijo que lo único que tenía era su auto estacionado en el antejardín, por lo que les entregó las llaves.\nDe ese modo, los delincuentes sacaron el vehículo y se dieron a la fuga.\nEl capitán de Carabineros, Patricio Riffo, indicó que los sujetos portaban armas de fuego.Por el momento, no hay detenidos y se trabaja en dar con el paradero de los responsables.",
                    autores: [
                        "Christian Borcoski"
                    ],
                    ubicacion: "Cerro Navia",
                    imagen: "https://media.biobiochile.cl/wp-content/uploads/2023/09/social-robo-cerro-navia.jpg"
                },
                {
                    titulo: "Murió víctima de brutal ataque en Lo Barnechea",
                    fecha_extraccion: "2025-06-20 15:38:00",
                    fecha_publicacion: "2023-12-02 14:14:00",
                    keywords: [
                        "delito",
                        "asalto",
                        "crimen de odio",
                        "fallecido"
                    ],
                    pagina: "Radio Cooperativa",
                    hipervinculo: "https://cooperativa.cl/noticias/pais/policial/homicidios/murio-victima-de-brutal-ataque-en-lo-barnechea/2023-12-02/142316.html",
                    texto: "El Movimiento de Integración y Liberación Homosexual (Movilh) informó de la muerte de Sandra Almeida Lizama, quien fue víctima de brutal ataque el pasado lunes en Lo Barnechea, motivado por su expresión de género y a manos de un hombre que ya antes la había hostigado e insultado.\n\"Este un final triste de una larga agonía de seis días. Expresamos nuestras condolencias a familia por este brutal crimen de odio, que suma un nombre más a larga lista de las víctimas de la homo/transfobia en Chile. Llamamos a las personas, a la sociedad y a las autoridades a condenar este abuso con la máxima fuerza\", señaló el dirigente Rolando Jiménez.\nPor su parte, la directora ejecutiva de Fundación Iguales, María José Cumplido, lamentó la situación y señaló que \n\"queremos darle todo el soporte a la familia\", además que espera que se esclarezca el caso \"para que estos crímenes no sigan ocurriendo en nuestro país\".\nSobre el agresor, hasta ahora identificado con la iniciales C.A.P.P., la organización aseguró que \"su prontuario es largo\", por la querella que presentará el Movilh buscará que se logre la pena de cadena perpetua en su contra, pues usó golpes de pie, puño y con una pala la golpeó en la cabeza.",
                    autores: [
                        "Cooperativa.cl"
                    ],
                    ubicacion: "Lo Barnechea",
                    imagen: "https://cooperativa.cl/noticias/site/artic/20231202/imag/foto_0000000120231202142316.jpg"
                },
                {
                    titulo: "“Guatón Mutema”: el crimen que paralizó a Quilicura",
                    fecha_extraccion: "2025-06-20 15:38:00",
                    fecha_publicacion: "2025-04-28 09:00:00",
                    keywords: [
                        "delito",
                        "tiroteo",
                        "fallecido"
                    ],
                    pagina: "La Tercera",
                    hipervinculo: "https://www.latercera.com/nacional/noticia/guaton-mutema-el-origen-que-habria-detras-del-crimen-que-paralizo-a-quilicura/",
                    texto: "Carlos Humberto Acevedo Ramírez (40), alias el \"Guatón Mutema\", era un sujeto conocido en la villa Pucará, en Quilicura. Una \"leyenda\", dicen sus familiares. Hincha acérrimo de la Universidad de Chile, durante la tarde se reunió con otros vecinos de la comuna para ver el partido de su club, que ayer se enfrentó a Palestino.\n\nDispusieron un televisor afuera de un domicilio en Calle 1 con Río Loa, donde vieron el encuentro. Como un buen número de personas del sector es seguidor de \"La U\", hacían esa actividad cada vez que jugaba el club. De hecho, a veces cerraban las calles cercanas.\n\nEl partido de este domingo había terminado cuando, de pronto, un vehículo color negro, tipo sedán sin patentes, apareció en esa intersección. Los vidrios del vehículo se bajaron y un número indeterminado de sujetos propinó al menos nueve balazos directos a Acevedo.\n\nAcevedo, quien es padre del cantante urbano Dehilan, fue llevado rápidamente por sus familiares hasta el Centro Comunitario de Salud Familiar (Cecosf) de la Villa Pucará. Allí se confirmó su deceso.\n\nEl caso respondería, según la policía, a un ajuste de cuentas entre bandas narcotraficantes. De hecho, el antecedente más cercano se vincula directamente al secuestro de la familia de otro presunto delincuente, donde el \"Guatón Mutema\" habría ejercido un rol clave.\n\nEl secuestro y otros delitos\nSegún fuentes policiales, Acevedo tuvo vinculación a un secuestro ocurrido en enero de este año. Por esos días se concretó el plagio a la familia de un sujeto perteneciente al clan de Los Mella que hoy se encuentra en la cárcel.\n\nEn ese sentido, quien lideró el secuestro fue Juan Pablo Díaz Arce, alias \"el Aguja\". Este sujeto heredó la peligrosa banda de los Cogote de Toro cuando Vladimir Soto Riquelme, \"el Cogote de Toro\", fuera asesinado en agosto del 2020.\n\nEl rol del \"Guatón Mutema\" habría sido entregar información de la familia del \"Mella\" para que se concretara dicho acto.\n\nPor ese hecho la banda de \"el Aguja\" pidió un monto de $500 millones, los cuales fueron cancelados por el sujeto afectado. De hecho, inicialmente había pedido $1.000 millones, pero al no alcanzar la cifra este la \"rebajó\" al monto pagado.\n\nAcevedo cuenta con amplio historial delictual relacionado al tráfico de drogas. En 2020 permaneció tras las rejas luego de que la Fiscalía Centro Norte lo investigara por los delitos de tráfico de drogas y lavado de activos. El rol de Acevedo estaba vinculado a la logística en el traslado de 40 kilos de marihuana tipo creepy desde el norte a la capital. Esa vez la policía incautó desde su domicilio un millón de pesos, una caja de municiones, 27 municiones calibre 9 milímetros y dos autos de alta gama: un Audi y un Mercedes Benz.\n\nEn otro domicilio relacionado a Acevedo también se decomisaron un arma de fuego marca Famae con 17 municiones de 9 milímetros. El arma mantenía encargo por robo.\n\nSegún una publicación de Ciper de 2020, el \"Guatón Mutema\" mantenía vínculos con carabineros de la 49° Comisaría de Quilicura que facilitaban su actuar.\n\n\"Viene una más grande\"\nLa Fiscalía Ecoh llegó hasta el lugar y ordenó que el caso sea investigado por la Brigada de Homicidios de la Policía de Investigaciones.\n\nEl fiscal Rodrigo Moya señaló el domingo que \"se están realizando todas las pericias correspondientes, esto es levantamiento de evidencia balística, como también el trabajo en el cuerpo de la víctima\".\n\nDurante la noche del domingo, un buen número de personas, entre familiares y amigos, llegó hasta el centro médico donde estaba Acevedo. Acusaron que el personal médico no prestó el auxilio suficiente para mantener con vida al fallecido.\n\nEl hecho originó un amplio operativo de Carabineros en el sector. El funeral, de hecho, será considerado como de \"alto riesgo\". Así lo señaló la alcaldesa de la comuna, Paulina Bobadilla, tras reunirse con el subsecretario de Seguridad Pública, Rafael Collado.\n\nEn ese orden, este lunes dos colegios de Quilicura suspendieron sus clases: la Escuela Pucará de Lasana y la Escuela Valle de la Luna. Durante la tarde de este lunes el ministro de Seguridad, Luis Cordero, se movilizó hasta la comuna para reunirse con la alcaldesa.\n\nPese a todo, su familia, un hermano y una hija del sujeto, enfrentaron las cámaras de Chilevisión para rechazar que Acevedo hubiese sido un narco del sector y que el caso se tratara de un ajuste de cuentas.\n\nAtribuyeron el ataque a un hecho fortuito y que el fallecido se interpuso al tiroteo para que no fueran alcanzados con las balas los menores que se encontraban viendo el partido de fútbol.\n\nEso sí, sin entregar más detalles, el hermano del sujeto, identificado como \"Cristián\", remató: \"Esto no va a quedar en vano. Esto va a venir más grande ahora\".\n\nEn tanto, Dehilan, quien no se encuentra en Chile, se refirió al hecho en sus redes sociales: \"Te amo, compañero mío, yo tu hijo. Siempre fuiste mi compañero y mi mejor amigo. Me duele verte por el teléfono, pero ya voy a llegar a casa, estar con la familia\".\n\nRefuerzo policial\nCordero este lunes visitó la comisaría de Quilicura y luego asistió a la Municipalidad de Quilicura para reunirse con la alcaldesa Bobadilla. Tras cartón, anunció que este mismo lunes se dispondría un refuerzo de Carabineros en la comuna.\n\n\"Este es un funeral que ha sido catalogado como de extremo riesgo. Le hemos informado (a la jefa comunal) de las medidas que se están adoptando, la alcaldesa nos ha transmitido sus principales inquietudes\", dijo el ministro, y agregó que ese refuerzo estará integrado por radiopatrullas, control de orden público y Gope.",
                    autores: ["Juan Pablo Andrews", "María Catalina Batarce"],
                    ubicacion: "Quilicura",
                    imagen: "https://www.latercera.com/resizer/v2/6MPARINIJ5BXDO6DMJN6RYHHXU.jpeg?auth=f597d2faa93a6d09ef9834c451a0f4a8eb2b0b9c1848a89f91b28e72fc8d3e15&smart=true&width=800&height=450&quality=70"
                },
            ]
        }
    },

    methods: {
        getLogo(pagina) {
            const logos = {
                "BioBio Chile": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxaKtXVa_5rXYa3Jv-L65j6h9xNofU4oeTkw&s",
                "CNN Chile": "https://upload.wikimedia.org/wikipedia/commons/0/04/Logo_cnnchile.png",
                "La Tercera": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzn9W65Z27kiAcLB-2YZysqTSS_EDoqvCtng&s",
                "CHV Noticias": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Logo_CHV_2015.png",
                "Mega Noticias": "https://static-cdn.jtvnw.net/jtv_user_pictures/6c5d6466-2ab2-4bf7-9e4d-79b156e08823-profile_image-300x300.png",
                "Radio Cooperativa": "https://app.cooperativa.cl/apps/site/artic/20220718/imag/foto_0000001220220718133642.png",
                "T13": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Logotipo_de_Teletrece.svg/1200px-Logotipo_de_Teletrece.svg.png",
            }
            return logos[pagina] || "https://i.pinimg.com/1200x/7b/71/35/7b7135945421f5d2a7e3b11830f8f227.jpg"
        },
        dibujarPoligonoPrueba() {
            const coords = [
                [
                    -70.693941,
                    -33.380316
                ],
                [
                    -70.6948677,
                    -33.3782288
                ],
                [
                    -70.6965889,
                    -33.3743679
                ],
                [
                    -70.6967985,
                    -33.3738977
                ],
                [
                    -70.6974748,
                    -33.3723805
                ],
                [
                    -70.6982848,
                    -33.3706076
                ],
                [
                    -70.6990814,
                    -33.3688436
                ],
                [
                    -70.6998727,
                    -33.3670717
                ],
                [
                    -70.7002603,
                    -33.3661925
                ],
                [
                    -70.6994146,
                    -33.3660363
                ],
                [
                    -70.6985563,
                    -33.3659657
                ],
                [
                    -70.6981258,
                    -33.3659422
                ],
                [
                    -70.6972246,
                    -33.3659277
                ],
                [
                    -70.6938302,
                    -33.3658997
                ],
                [
                    -70.6931825,
                    -33.3659254
                ],
                [
                    -70.6900497,
                    -33.3661382
                ],
                [
                    -70.6889057,
                    -33.3662189
                ],
                [
                    -70.68936,
                    -33.3653523
                ],
                [
                    -70.6895561,
                    -33.3649073
                ],
                [
                    -70.6896098,
                    -33.3646385
                ],
                [
                    -70.6896433,
                    -33.3641759
                ],
                [
                    -70.6897774,
                    -33.3628766
                ],
                [
                    -70.6900209,
                    -33.3620112
                ],
                [
                    -70.6901872,
                    -33.3614982
                ],
                [
                    -70.6916705,
                    -33.3572618
                ],
                [
                    -70.6919494,
                    -33.3563769
                ],
                [
                    -70.6921184,
                    -33.3556196
                ],
                [
                    -70.6922498,
                    -33.3549206
                ],
                [
                    -70.6924215,
                    -33.3539909
                ],
                [
                    -70.6925342,
                    -33.3534957
                ],
                [
                    -70.6926817,
                    -33.3530118
                ],
                [
                    -70.6928828,
                    -33.3524718
                ],
                [
                    -70.6930491,
                    -33.3521134
                ],
                [
                    -70.6923161,
                    -33.3517075
                ],
                [
                    -70.6915436,
                    -33.3508113
                ],
                [
                    -70.6902562,
                    -33.3494849
                ],
                [
                    -70.688797,
                    -33.3478717
                ],
                [
                    -70.6880675,
                    -33.3465094
                ],
                [
                    -70.6875954,
                    -33.3450754
                ],
                [
                    -70.6875096,
                    -33.3434263
                ],
                [
                    -70.6870375,
                    -33.342279
                ],
                [
                    -70.6858788,
                    -33.340845
                ],
                [
                    -70.6844626,
                    -33.3400562
                ],
                [
                    -70.6830893,
                    -33.339877
                ],
                [
                    -70.6815853,
                    -33.3391839
                ],
                [
                    -70.6801281,
                    -33.3379768
                ],
                [
                    -70.6799994,
                    -33.3373314
                ],
                [
                    -70.6807719,
                    -33.3353953
                ],
                [
                    -70.680787,
                    -33.3331819
                ],
                [
                    -70.6810445,
                    -33.3319628
                ],
                [
                    -70.681242,
                    -33.3309445
                ],
                [
                    -70.6814718,
                    -33.3307815
                ],
                [
                    -70.6820929,
                    -33.3303571
                ],
                [
                    -70.6822871,
                    -33.3301803
                ],
                [
                    -70.6825516,
                    -33.3299246
                ],
                [
                    -70.682565,
                    -33.3297126
                ],
                [
                    -70.6826106,
                    -33.3296145
                ],
                [
                    -70.6836591,
                    -33.3293122
                ],
                [
                    -70.6848481,
                    -33.3290749
                ],
                [
                    -70.685997,
                    -33.3288096
                ],
                [
                    -70.6871969,
                    -33.3286935
                ],
                [
                    -70.6877845,
                    -33.3286283
                ],
                [
                    -70.6885545,
                    -33.3283687
                ],
                [
                    -70.6896137,
                    -33.3275738
                ],
                [
                    -70.6901448,
                    -33.3259248
                ],
                [
                    -70.6902151,
                    -33.3254896
                ],
                [
                    -70.6901011,
                    -33.3246435
                ],
                [
                    -70.6913467,
                    -33.3237659
                ],
                [
                    -70.6919915,
                    -33.3237222
                ],
                [
                    -70.6928951,
                    -33.3238253
                ],
                [
                    -70.6931253,
                    -33.3237934
                ],
                [
                    -70.6947233,
                    -33.323163
                ],
                [
                    -70.6950945,
                    -33.3229566
                ],
                [
                    -70.6959665,
                    -33.3222472
                ],
                [
                    -70.696382,
                    -33.321424
                ],
                [
                    -70.6967811,
                    -33.321223
                ],
                [
                    -70.6978097,
                    -33.3203072
                ],
                [
                    -70.6984953,
                    -33.3199571
                ],
                [
                    -70.6993552,
                    -33.3196532
                ],
                [
                    -70.700541,
                    -33.3194338
                ],
                [
                    -70.7037316,
                    -33.3192234
                ],
                [
                    -70.7054053,
                    -33.318829
                ],
                [
                    -70.7082806,
                    -33.3181117
                ],
                [
                    -70.7102118,
                    -33.3183986
                ],
                [
                    -70.7108984,
                    -33.3185421
                ],
                [
                    -70.7113132,
                    -33.31868
                ],
                [
                    -70.711236,
                    -33.3189465
                ],
                [
                    -70.711126,
                    -33.3191231
                ],
                [
                    -70.7109847,
                    -33.3192934
                ],
                [
                    -70.710805,
                    -33.3194438
                ],
                [
                    -70.7105495,
                    -33.3195676
                ],
                [
                    -70.7102251,
                    -33.3197233
                ],
                [
                    -70.7100242,
                    -33.3198352
                ],
                [
                    -70.7098524,
                    -33.3199591
                ],
                [
                    -70.7096597,
                    -33.3201763
                ],
                [
                    -70.7094717,
                    -33.3204537
                ],
                [
                    -70.7091504,
                    -33.3210172
                ],
                [
                    -70.7087013,
                    -33.3217918
                ],
                [
                    -70.708674,
                    -33.3218916
                ],
                [
                    -70.7190133,
                    -33.3244245
                ],
                [
                    -70.7366797,
                    -33.3283941
                ],
                [
                    -70.7530756,
                    -33.3320486
                ],
                [
                    -70.7602082,
                    -33.3336384
                ],
                [
                    -70.766463,
                    -33.3352426
                ],
                [
                    -70.7916876,
                    -33.341255
                ],
                [
                    -70.7974822,
                    -33.3393442
                ],
                [
                    -70.7987462,
                    -33.3445879
                ],
                [
                    -70.7991753,
                    -33.3453622
                ],
                [
                    -70.799862,
                    -33.3462226
                ],
                [
                    -70.8015528,
                    -33.3473196
                ],
                [
                    -70.8036344,
                    -33.3503552
                ],
                [
                    -70.8019171,
                    -33.3513505
                ],
                [
                    -70.8013382,
                    -33.351686
                ],
                [
                    -70.794283,
                    -33.3569411
                ],
                [
                    -70.7879057,
                    -33.3617443
                ],
                [
                    -70.7854681,
                    -33.3635866
                ],
                [
                    -70.7821736,
                    -33.3661208
                ],
                [
                    -70.7794905,
                    -33.3682844
                ],
                [
                    -70.773242,
                    -33.3730869
                ],
                [
                    -70.7717022,
                    -33.3740896
                ],
                [
                    -70.7692051,
                    -33.3754492
                ],
                [
                    -70.7682295,
                    -33.3759182
                ],
                [
                    -70.7639804,
                    -33.378058
                ],
                [
                    -70.7596818,
                    -33.3813954
                ],
                [
                    -70.7575991,
                    -33.3830897
                ],
                [
                    -70.756624,
                    -33.3834509
                ],
                [
                    -70.7562108,
                    -33.3836721
                ],
                [
                    -70.7546833,
                    -33.3843334
                ],
                [
                    -70.7532867,
                    -33.3848348
                ],
                [
                    -70.751191,
                    -33.3855509
                ],
                [
                    -70.7509556,
                    -33.3858278
                ],
                [
                    -70.7508011,
                    -33.3865301
                ],
                [
                    -70.7507411,
                    -33.3871035
                ],
                [
                    -70.7504406,
                    -33.3876911
                ],
                [
                    -70.7500802,
                    -33.3883361
                ],
                [
                    -70.749857,
                    -33.3889954
                ],
                [
                    -70.7500287,
                    -33.3896619
                ],
                [
                    -70.7501608,
                    -33.3900047
                ],
                [
                    -70.7501145,
                    -33.3905219
                ],
                [
                    -70.7499514,
                    -33.3907727
                ],
                [
                    -70.749136,
                    -33.39083
                ],
                [
                    -70.7479773,
                    -33.390701
                ],
                [
                    -70.7457028,
                    -33.3897694
                ],
                [
                    -70.7444153,
                    -33.3893394
                ],
                [
                    -70.7431279,
                    -33.3890886
                ],
                [
                    -70.7412825,
                    -33.3893036
                ],
                [
                    -70.7400809,
                    -33.3893036
                ],
                [
                    -70.7389651,
                    -33.3899486
                ],
                [
                    -70.7382784,
                    -33.3908085
                ],
                [
                    -70.7370339,
                    -33.3927792
                ],
                [
                    -70.7364331,
                    -33.3930301
                ],
                [
                    -70.7357464,
                    -33.3928867
                ],
                [
                    -70.7343302,
                    -33.3925643
                ],
                [
                    -70.7320128,
                    -33.3919193
                ],
                [
                    -70.7301812,
                    -33.3920872
                ],
                [
                    -70.7285083,
                    -33.391747
                ],
                [
                    -70.7257901,
                    -33.3916327
                ],
                [
                    -70.7234297,
                    -33.3915968
                ],
                [
                    -70.7210265,
                    -33.3917043
                ],
                [
                    -70.7148896,
                    -33.3915252
                ],
                [
                    -70.7122288,
                    -33.3910594
                ],
                [
                    -70.7110701,
                    -33.3905935
                ],
                [
                    -70.7096968,
                    -33.3890169
                ],
                [
                    -70.708066,
                    -33.3873328
                ],
                [
                    -70.7060919,
                    -33.3856486
                ],
                [
                    -70.7047186,
                    -33.3843228
                ],
                [
                    -70.7034741,
                    -33.3833194
                ],
                [
                    -70.6961785,
                    -33.3824235
                ],
                [
                    -70.6955276,
                    -33.3823082
                ],
                [
                    -70.6952773,
                    -33.381886
                ],
                [
                    -70.6942902,
                    -33.3808826
                ],
                [
                    -70.693941,
                    -33.380316
                ]
            ];

            const opciones = {
                color: 'purple',
                fillColor: 'purple',
                fillOpacity: 0.4,
            };

            // Accede al método de Map.vue a través del ref
            this.$refs.map.putPolygon(coords, opciones, true, true);
        },
    },

    mounted() {
        setTimeout(() => {
            this.dibujarPoligonoPrueba();
        }, 500);
        // Puedes cargar datos desde API aquí si lo deseas
    }
}
</script>

<style scoped>
.fill-height {
    height: 100vh;
}

.scrollable-news {
    overflow-y: auto;
    flex-grow: 1;
    max-height: 73vh;
    /* Ajusta si tu app-bar mide distinto */
}

.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.truncate-multiline {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.scrollable-news::-webkit-scrollbar {
    width: 20px;
}

.scrollable-news::-webkit-scrollbar-track {
    background: #f0ccc4;
    /* Fondo del scrollbar */
    border-radius: 4px;
}

.scrollable-news::-webkit-scrollbar-thumb {
    background-color: #e53e3e;
    /* Rojo brillante */
    border-radius: 6px;
    border: 2px solid transparent;
    /* Para espacio alrededor del thumb */
    background-clip: content-box;
}

.scrollable-news::-webkit-scrollbar-thumb:hover {
    background-color: #c53030;
    /* Rojo oscuro al pasar el mouse */
}
</style>
