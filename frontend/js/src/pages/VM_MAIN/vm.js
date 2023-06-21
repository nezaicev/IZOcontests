import Box from "@mui/material/Box";
import React from "react";
import {createSvgIcon} from "@mui/material";


const HomeIcon = createSvgIcon(
    <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>,
    'Home',
);

// const rectStyle={
//     #box:hover {
//   box-shadow: 0 10px blue;
//   transition: box-shadow 0.3s;
// }
// }



const VM = (props) => {
    const [isHover, setHover] = React.useState(false)

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
                <line id="line-5" x1="2" y1="48" x2="208.38988" y2="48" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>
                <line id="line-6" x1="2" y1="84.5" x2="205.38988" y2="84.5" stroke={"#3C3C3B"}
                      strokeWidth={0.65}/>


                <rect

                    fill={"#c56464"}
                    id="rect4433"
                    width="35.522415"
                    height="34.805302"
                    x="88.556702"
                    y="49.049023"/>


                <rect
                    fill={"#d1d5ed"}
                    id="rect4433-6"
                    width="35.522415"
                    height="34.805302"
                    x="126.42439"
                    y="49.420052"/>

                <rect

                    fill={"#a2d5b4"}
                    id="rect4433-2"
                    width="35.522415"
                    height="34.805302"
                    x="51.219578"
                    y="49.528976"/>
                <rect

                    fill={"#c5a764"}
                    id="rect4433-5"
                    width="35.522415"
                    height="34.805302"
                    x="88.524529"
                    y="11.986798"/>
                <rect

                    fill={"#409daa"}
                    id="rect4433-5-4"
                    width="35.522415"
                    height="34.805302"
                    x="51.426331"
                    y="13.008327"/>

                <rect

                    fill={"#cfb7a7"}
                    id="rect4433-5-5"
                    width="35.522415"
                    height="34.805302"
                    x="126.24857"
                    y="13.156378"/>
                <rect

                    fill={"#a5cadd"}
                    id="rect4433-5-5-1"
                    width="35.522415"
                    height="34.805302"
                    x="163.8093"
                    y="12.828334"/>
                <rect

                    fill={"#c6c8f0"}
                    id="rect4433-5-5-4"
                    width="35.522415"
                    height="34.805302"
                    x="13.615749"
                    y="49.165684"/>
                <rect

                    fill={"#d0edd0"}
                    id="rect4433-5-5-0"
                    width="35.522415"
                    height="34.805302"
                    x="163.57405"
                    y="49.243557"/>
                <rect

                    fill={"#9cbde3"}
                    id="rect4433-5-5-46"
                    width="35.522415"
                    height="34.805302"
                    x="88.432693"
                    y="85.967056"/>
                <rect

                    fill={"#d5c68e"}
                    id="rect4433-5-5-9"
                    width="35.522415"
                    height="34.805302"
                    x="125.55808"
                    y="86.0952"/>
                <rect

                    fill={"#e0adad"}
                    id="rect4433-7"
                    width="35.522415"
                    height="34.805302"
                    x="13.808679"
                    y="86.219551"/>
                <rect

                    fill={"#b1e2cc"}
                    id="rect4433-7-8"
                    width="35.522415"
                    height="34.805302"
                    x="163.45549"
                    y="86.163292"/>
                <rect

                    fill={"#64bcc5"}
                    id="rect4433-9"
                    width="35.522415"
                    height="34.805302"
                    x="51.423767"
                    y="86.044823"/>


                <a href="#" id="rect-1" className='rectMainPage'>
                    <g>
                        <rect

                            fill={"#d2a586"}
                            id="rect4433-5-4-8"
                            width="35.522415"
                            height="34.805302"
                            x="13.206748"
                            y="12.506952"/>
                        <text x="30" y="30" fill={"#3C3C3B"} fontSize={5} textAnchor="middle">
                            <tspan>Конкурс</tspan>
                            <tspan x="30" dy="1em">Артакиада</tspan>
                        </text>
                    </g>
                </a>


            </svg>

        </Box>



        //  <Box sx={{fontFamily: 'Roboto', height: 'auto',  justifyContent: 'center'}}>
        //
        //      <svg viewBox="0 0 1000 1000" width="100%" height="100%">
        //          <g>
        //              <g transform='translate(460,100)'>
        //                  <rect  width="80" height="80"
        //                        fill="skyblue"
        //                  />
        //                  <text x="5" y="10" fontSize="20"> Музей</text>
        //              </g>
        //          </g>
        //
        //          <rect
        // // style="opacity:1;fill:#1a1a1a;fill-opacity:1;stroke:none;stroke-width:12.8233;stroke-opacity:1"
        // //              strokeWidth="12"
        // //              fill="#1a1a1a"
        // style={{ fill: '#3C3C3B',opacity: 1 }}
        // id="rect4322"
        // width="1.45531863"
        // height="124.71623"
        // x="49.836937"
        // y="5.921608" />
        //
        //          {/*<line x1="5" y1="60" x2="100" y2="60" stroke="black" stroke-width="0.5" />*/}
        //      </svg>
        //
        //  </Box>

    )
}

export {VM}