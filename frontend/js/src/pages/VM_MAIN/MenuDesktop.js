import React from "react";
import {BoxButtonLink} from "./BoxButtonLink";


const fontSize = 4

const MenuDesktop =()=>{
    return(
        <>

        <svg width='93%' height="95%" viewBox="-14 0 250 150">


                <line id="line-0" x1="106" y1="0" x2="106" y2="11"
                      stroke={"#3C3C3B"} strokeWidth={0.6}/>
                <line id="line-1" x1="49.836937" y1="5.921608" x2="49.836937" y2="125.71623"
                      stroke={"#3C3C3B"} strokeWidth={0.8}/>
                <line id="line-2" x1="87.534067" y1="10.921608" x2="87.534067" y2="133.71623"
                      stroke={"#3C3C3B"} strokeWidth={0.75}/>
                <line id="line-3" x1="124.69011" y1="11.0827985" x2="124.69011" y2="133.40666"
                      stroke={"#3C3C3B"} strokeWidth={0.75}/>
                <line id="line-4" x1="162.38988" y1="7.3414125" x2="162.38988" y2="122.51492"
                      stroke={"#3C3C3B"} strokeWidth={0.75}/>
                <line id="line-5" x1="0" y1="48" x2="208.38988" y2="48" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>
                <line id="line-6" x1="2" y1="84.5" x2="205.38988" y2="84.5" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>
                <line id="line-7" x1="2" y1="11" x2="205.38988" y2="11" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>





                <BoxButtonLink active={true} href='events' color={'rgb(212, 212, 210)'}>
                    <rect
                        id="rect4433-5-4-1"
                        width="53.522415"
                        height="10"
                        x="51.5"
                        y="0"
                        rx={0.5}
                    />

                    <text x="79" y="6.5" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">

                        <tspan>МЕРОПРИЯТИЯ</tspan>


                    </text>
                </BoxButtonLink>

             <BoxButtonLink active={true} href='admin' color={'rgb(212, 212, 210)'}>
                    <rect
                        id="rect4433-8"
                        width="53.522415"
                        height="10"
                        x="107"
                        y="0"
                        rx={0.5}
                    />

                    <text x="134.5" y="6.5" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">

                        <tspan>ЛИЧНЫЙ КАБИНЕТ</tspan>

                    </text>
                </BoxButtonLink>







                <BoxButtonLink active={true} href='artakiada' color={'rgba(64,157,170,0.76)'}>
                    <rect
                        id="rect4433-5-4"
                        width="35.522415"
                        height="34.805302"
                        x="50.926331"
                        y="12.008327"
                        rx={0.5}
                    />

                    <text x="69.5" y="25.5" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">

                        <tspan>АРТАКИАДА</tspan>
                        <tspan x="69.5" dy="1.5em">«ИЗОБРАЖЕНИЕ</tspan>
                        <tspan x="69.5" dy="1.5em">И СЛОВО»</tspan>

                    </text>
                </BoxButtonLink>

                <BoxButtonLink active={true} href='mymoskvichi' color={'rgba(224,173,173,0.76)'}>

                    <rect
                        id="rect4433-5-4-8"
                        width="41.522415"
                        height="34.805302"
                        x="7.206748"
                        y="12.008327"
                        rx={0.5}
                    />

                    <text x="28" y="25.5" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="28" dy="1.5em">МУЛЬТИМЕДИА</tspan>
                        <tspan x="28" dy="1.5em">«МЫ МОСКВИЧИ»</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink active={true} href='nrusheva' color={'rgba(197,167,100,0.76)'}>
                    <rect

                        id="rect4433-5"
                        width="35.522415"
                        height="34.805302"
                        x="88.524529"
                        y="12.008327"
                        rx={0.5}
                    />

                    <text x="106.5" y="25.5" fill={"#3C3C3B"} fontSize={fontSize}
                          textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="106.5" dy="1.5em">ИМЕНИ</tspan>
                        <tspan x="106.5" dy="1.5em">НАДИ РУШЕВОЙ</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink active={true} href='cherez_iskusstvo' color={'rgba(207,183,167,0.76)'}>
                    <rect
                        id="rect4433-5-5"
                        width="35.522415"
                        height="34.805302"
                        x="125.84857"
                        y="12.008327"
                        rx={0.5}
                    />

                    <text x="144.5" y="23.5" fill={"#3C3C3B"} fontSize={fontSize}
                          textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="144.5" dy="1.5em">«ЧЕРЕЗ</tspan>
                        <tspan x="144.5" dy="1.5em">ИСКУССТВО</tspan>
                        <tspan x="144.5" dy="1.5em">К ЖИЗНИ»</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'rgba(165,202,221,0.76)'}>
                    <rect

                        id="rect4433-5-5-1"
                        width="41.522415"
                        height="34.805302"
                        x="163.45549"
                        y="12.008327"
                        rx={0.5}
                    />

                    <text x="183" y="23.5" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="184" dy="1.5em">«ИЗОБРАЗИТЕЛЬНЫЙ</tspan>
                        <tspan x="183" dy="1.5em">ДИКТАНТ»</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink active={true} href='museum' color={'rgba(197,100,100,0.76)'}>
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
                        <tspan x="106.5" fontSize={3.1} dy="8.5em">ШКОЛА НЕМЕНСКОГО</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink active={true} href='video' color={'rgba(198,200,240,0.76)'}>
                    <rect

                        id="rect4433-5-5-4"
                        width="41.522415"
                        height="34.805302"
                        x="7.615749"
                        y="49.165684"
                        rx={0.5}
                    />

                    <text x="29" y="66.5" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={fontSize}>ВИДЕОМАТЕРИАЛЫ</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink active={true} href='expositions/main' color={'#a2d5b4'}>
                    <rect
                        id="rect4433-2"
                        width="35.522415"
                        height="34.805302"
                        x="51.219578"
                        y="49.128976"
                        rx={0.5}
                    />

                    <text x="69.6" y="66.5" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={fontSize}>ВЫСТАВКИ</tspan>
                    </text>
                </BoxButtonLink>


                <BoxButtonLink active={true} href='publication' color={'rgba(209,213,237,0.76)'}>
                    <rect
                        id="rect4433-6"
                        width="35.522415"
                        height="34.805302"
                        x="126"
                        y="49.420052"
                        rx={0.5}
                    />
                    <text x="144.5" y="66.5" fill={"#3C3C3B"} textAnchor="middle">
                        <tspan fontSize={fontSize}>ИЗДАНИЯ</tspan>
                    </text>
                </BoxButtonLink>

                <BoxButtonLink active={true} href='art_challenge' color={'rgba(208,237,208,0.76)'}>
                    <rect

                        id="rect4433-5-5-0"
                        width="41.522415"
                        height="34.805302"
                        x="163.45549"
                        y="49.243557"
                        rx={0.5}
                    />
                    <text x="183" y="66.5" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>АРТ-АКЦИИ</tspan>

                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='#' color={'rgba(140,188,243,0.76)'}>
                    <rect
                        id="rect4433-7"
                        width="41.522415"
                        height="34.805302"
                        x="7.615749"
                        y="86.219551"
                        rx={0.5}
                    />
                    <text x="29" y="98" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>ПЕДАГОГИЧЕСКИЕ</tspan>
                        <tspan x="29" dy="1.5em">МЕТОДИЧЕСКИЕ</tspan>
                        <tspan x="29" dy="1.5em">КОЛЛЕКЦИИ</tspan>

                    </text>
                </BoxButtonLink>


                <BoxButtonLink href='#' color={'rgba(100,188,197,0.76)'}>
                    <rect
                        id="rect4433-9"
                        width="35.522415"
                        height="34.805302"
                        x="50.923767"
                        y="86.044823"
                        rx={0.5}
                    />
                    <text x="69" y="98" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">

                        <tspan>СКАЗКИ</tspan>
                        <tspan x="69" dy="1.5em">НАРОДОВ МИРА</tspan>
                        <tspan x="69" dy="1.5em">ГЛАЗАМИ ДЕТЕЙ</tspan>
                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='art_project' active={true} color={'rgba(156,189,227,0.76)'}>
                    <rect
                        id="rect4433-5-5-46"
                        width="35.522415"
                        height="34.805302"
                        x="88.432693"
                        y="85.967056"
                        rx={0.5}
                    />
                    <text x="106" y="100" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>КОНКУРС</tspan>
                        <tspan x="106" dy="1.5em">«АРТ-ПРОЕКТ»</tspan>
                    </text>
                </BoxButtonLink>

                <BoxButtonLink href='#' color={'rgba(213,198,142,0.76)'}>
                    <rect

                        id="rect4433-5-5-9"
                        width="35.522415"
                        height="34.805302"
                        x="125.95808"
                        y="86.0952"
                        rx={0.5}
                    />
                    <text x="144" y="100" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>ПРОЕКТ</tspan>
                        <tspan x="144" dy="1.5em">«ДИЗАЙН ДЕТЯМ»</tspan>
                    </text>
                </BoxButtonLink>

                <BoxButtonLink active={true} href='vp' color={'rgba(177,226,204,0.76)'}>
                    <rect
                        id="rect4433-7-8"
                        width="41.522415"
                        height="34.805302"
                        x="163.45549"
                        y="86.163292"
                        rx={0.5}
                    />
                    <text x="184" y="100" fill={"#3C3C3B"} fontSize={fontSize} textAnchor="middle">
                        <tspan>ХУДОЖЕСТВЕННЫЕ</tspan>
                        <tspan x="184" dy="1.5em">ПРОЕКТЫ</tspan>
                    </text>
                </BoxButtonLink>

            </svg>
        {/*    <svg width='73%' height="85%" viewBox="100 0 250 150">*/}
        {/*    <circle cx="60" cy="60" r="50"/>*/}
        {/*</svg>*/}
</>
    )



}

export {MenuDesktop}