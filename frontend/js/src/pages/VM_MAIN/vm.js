import Box from "@mui/material/Box";
import React, {useState} from "react";
import {createSvgIcon} from "@mui/material";


const HomeIcon = createSvgIcon(
    <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>,
    'Home',
);


const BoxButtonLink = (props) => {
    return (
        <a href={props.href} style={{
            fill: props.color,
            transition: '0.5s'
        }}
           onMouseEnter={(e) => {
               e.currentTarget.style.fill = '#fff'
           }}
           onMouseLeave={(e) => {
               e.currentTarget.style.fill = props.color
           }}>
            {props.children}

        </a>
    )
}


const VM = (props) => {

    return (
        <Box sx={{
            justifyContent: 'center',
            display: 'flex',
            alignItems: 'center',
            width: '100%',
            height: "100%",
            fontFamily: 'Roboto'
        }}>
            <svg width="73%" height="85%" viewBox="-14 8 250 150">


                <line id="line-1" x1="49.836937" y1="5.921608" x2="49.836937" y2="125.71623"
                      stroke={"#3C3C3B"} strokeWidth={0.8}/>
                <line id="line-2" x1="87.534067" y1="4.921608" x2="87.534067" y2="133.71623"
                      stroke={"#3C3C3B"} strokeWidth={0.75}/>
                <line id="line-3" x1="124.69011" y1="6.0827985" x2="124.69011" y2="133.40666"
                      stroke={"#3C3C3B"} strokeWidth={0.75}/>
                <line id="line-4" x1="162.38988" y1="7.3414125" x2="162.38988" y2="122.51492"
                      stroke={"#3C3C3B"} strokeWidth={0.75}/>
                <line id="line-5" x1="0" y1="48" x2="208.38988" y2="48" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>
                <line id="line-6" x1="2" y1="84.5" x2="205.38988" y2="84.5" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>




                 <BoxButtonLink href='#' color={'rgba(64,157,170,0.5)'}>
                    <rect
                        id="rect4433-5-4"
                        width="35.522415"
                        height="34.805302"
                        x="51.426331"
                        y="13.008327"
                        rx={0.5}
                    />

                    <text x="69.5" y="27" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">

                        <tspan>АРТАКИАДА</tspan>
                        <tspan x="69.5" dy="1.5em">«ИЗОБРАЖЕНИЕ</tspan>
                        <tspan x="69.5" dy="1.5em">И СЛОВО»</tspan>

                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='#' color={'rgba(64,110,170,0.5)'}>
                    <rect
                        id="rect4433-5-4-8"
                        width="40.522415"
                        height="34.805302"
                        x="8.206748"
                        y="12.506952"
                        rx={0.5}
                    />

                    <text x="28" y="25.5" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="28" dy="1.5em">МУЛЬТИМЕДИА</tspan>
                        <tspan x="28" dy="1.5em">«МЫ МОСКВИЧИ»</tspan>
                    </text>
                </BoxButtonLink>





                <BoxButtonLink href='#' color={'#c5a764'}>
                    <rect

                        id="rect4433-5"
                        width="35.522415"
                        height="34.805302"
                        x="88.524529"
                        y="11.986798"
                        rx={0.5}
                    />

                    <text x="106.5" y="25.5" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="106.5" dy="1.5em">ИМЕНИ</tspan>
                        <tspan x="106.5" dy="1.5em">НАДИ РУШЕВОЙ</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#cfb7a7'}>
                    <rect
                        id="rect4433-5-5"
                        width="35.522415"
                        height="34.805302"
                        x="126.24857"
                        y="13.156378"
                        rx={0.5}
                    />

                    <text x="144.5" y="23.5" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="144.5" dy="1.5em">«ЧЕРЕЗ</tspan>
                        <tspan x="144.5" dy="1.5em">ИССКУСТВО</tspan>
                        <tspan x="144.5" dy="1.5em">К ЖИЗНИ»</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#a5cadd'}>
                    <rect

                        id="rect4433-5-5-1"
                        width="40.522415"
                        height="34.805302"
                        x="162.8093"
                        y="12.828334"
                        rx={0.5}
                    />

                    <text x="183" y="23.5" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="183" dy="1.5em">«ИЗОБРАЗИТЕЛЬНЫЙ</tspan>
                        <tspan x="183" dy="1.5em">ДИКТАНТ»</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#c56464'}>
                    <rect
                        id="rect4433"
                        width="35.522415"
                        height="34.805302"
                        x="88.556702"
                        y="49.049023"
                        rx={0.5}
                    />

                    <line id="line-m-1" x1="88.556702" y1="56.5" x2="124.079117" y2="56.5"
                          stroke={"#3C3C3B"} strokeWidth={0.35}/>
                    <line id="line-m-2" x1="100.556702" y1="56.5" x2="100.556702" y2="76.5"
                          stroke={"#3C3C3B"} strokeWidth={0.4}/>
                    <line id="line-m-3" x1="113" y1="56.5" x2="113" y2="76.5" stroke={"#3C3C3B"}
                          strokeWidth={0.40}/>
                    <line id="line-m-1" x1="100.556702" y1="66.5" x2="113" y2="66.5"
                          stroke={"#3C3C3B"} strokeWidth={0.4}/>
                    <text x="106.5" y="55" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={4.5}>МУЗЕЙ</tspan>
                        <tspan x="106.5" fontSize={3.2} dy="8.5em">ШКОЛА НЕМЕНСКОГО</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#c6c8f0'}>
                    <rect

                        id="rect4433-5-5-4"
                        width="40.522415"
                        height="34.805302"
                        x="8.615749"
                        y="49.165684"
                        rx={0.5}
                    />

                    <text x="29" y="66.5" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={3.8}>ВИДЕОМАТЕРИАЛЫ</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#a2d5b4'}>
                    <rect
                        id="rect4433-2"
                        width="35.522415"
                        height="34.805302"
                        x="51.219578"
                        y="49.528976"
                        rx={0.5}
                    />

                    <text x="69.6" y="66.5" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={3.8}>ВЫСТАВКИ</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#d1d5ed'}>
                    <rect
                        id="rect4433-6"
                        width="35.522415"
                        height="34.805302"
                        x="126.42439"
                        y="49.420052"
                        rx={0.5}
                    />
                    <text x="144.5" y="66.5" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={3.8}>ИЗДАНИЯ</tspan>
                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='#' color={'#d0edd0'}>
                    <rect

                        id="rect4433-5-5-0"
                        width="40.522415"
                        height="34.805302"
                        x="162.87405"
                        y="49.243557"
                        rx={0.5}
                    />
                    <text x="183" y="61" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>ПЕДАГОГИЧЕСКИЕ</tspan>
                        <tspan x="183" dy="1.5em">МЕТОДИЧЕСКИЕ</tspan>
                        <tspan x="183" dy="1.5em">КОЛЛЕКЦИИ</tspan>
                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='#' color={'#e0adad'}>
                   <rect
                    id="rect4433-7"
                    width="40.522415"
                    height="34.805302"
                    x="8.615749"
                    y="86.219551"
                    rx={0.5}
                   />
                    <text x="29" y="98" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>СКАЗКИ</tspan>
                        <tspan x="29" dy="1.5em">НОРОДОВ МИРА</tspan>
                        <tspan x="29" dy="1.5em">ГЛАЗАМИ ДЕТЕЙ</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'#64bcc5'}>
                  <rect
                    id="rect4433-9"
                    width="35.522415"
                    height="34.805302"
                    x="51.423767"
                    y="86.044823"
                    rx={0.5}
                  />
                    <text x="69" y="98" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>АРТ-АКЦИИ</tspan>
                        {/*<tspan x="69" dy="1.5em">АКЦИИ</tspan>*/}
                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='#' color={'#9cbde3'}>
                <rect
                    id="rect4433-5-5-46"
                    width="35.522415"
                    height="34.805302"
                    x="88.432693"
                    y="85.967056"
                    rx={0.5}
                />
                    <text x="105" y="98" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="105" dy="1.5em">АРТ</tspan>
                        <tspan x="105" dy="1.5em">ПРОЕКТОВ</tspan>
                    </text>
                </BoxButtonLink>

                 <BoxButtonLink href='#' color={'#d5c68e'}>
                <rect

                    id="rect4433-5-5-9"
                    width="35.522415"
                    height="34.805302"
                    x="125.55808"
                    y="86.0952"
                    rx={0.5}
                />
                    <text x="142" y="98" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>АРТ</tspan>
                        <tspan x="142" dy="1.5em">ЧЕЛЛЕНДЖИ</tspan>
                    </text>
                </BoxButtonLink>

                 <BoxButtonLink href='#' color={'#b1e2cc'}>
                <rect
                    id="rect4433-7-8"
                    width="40.522415"
                    height="34.805302"
                    x="163.45549"
                    y="86.163292"
                    rx={0.5}
                />
                    <text x="182" y="98" fill={"#3C3C3B"} fontSize={3.8} textAnchor="middle">
                        <tspan>ПРОЕКТ</tspan>
                        <tspan x="182" dy="1.5em">«ДИЗАЙН ДЕТЯМ»</tspan>
                    </text>
                </BoxButtonLink>

            </svg>

        </Box>


    )
}

export {VM}