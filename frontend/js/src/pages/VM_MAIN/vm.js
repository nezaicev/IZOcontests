import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import {createSvgIcon} from "@mui/material";
import {MenuDesktop} from "./MenuDesktop";
import {MenuMobile} from "./MenuMobile";

const getSizeWindow = () => {

}



const HomeIcon = createSvgIcon(
    <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>,
    'Home',
);

const styleTexture = {
    backgroundColor: '#fff',
    backgroundImage: 'url(static/frontend/images/background/back.svg)',
    backgroundPositionX: 'center',
    backgroundPositionY: '85%',
    backgroundRepeat: 'no-repeat',
    backgroundAttachment: 'fixed',
    backgroundSize: 'cover',
    "&::before": {
        content: '""',
        position: 'absolute',
        zIndex: 1,
        top: 0,
        left: 0,
        display: 'block',
        width: '100%',
        height: '100%',
        pointerEvents: 'none',
        backgroundImage: 'url(https://cdn.selectel.ru/site/img/texture.91f8215.png)',
        backgroundSize: '260px',
        opacity: 0.35,
    }
}

const setTextureStyle = () => {
    document.body.classList.add('texture')
}

const setBackgroundStyle = () => {
    document.body.style.backgroundColor = "#fff";
    document.body.style.backgroundImage = 'url(static/frontend/images/background/back.svg)';
    document.body.style.backgroundPositionX = 'center'
    document.body.style.backgroundPositionY = '85%'
    document.body.style.backgroundRepeat = 'no-repeat'
    document.body.style.backgroundAttachment = 'fixed'
    document.body.style.backgroundSize = 'cover'
}


const BoxButtonLink = (props) => {
    return (
        <a href={props.href} style={{
            fill: props.color,
            transition: '0.5s',
            cursor: props.active ? 'hand' : 'default',
        }}
           onMouseEnter={(e) => {
               if (props.active) {
                   e.currentTarget.style.fill = '#fff'
               }
           }}
           onMouseLeave={(e) => {
               if (props.active) {
                   e.currentTarget.style.fill = props.color
               }
           }}>
            {props.children}

        </a>
    )
}


const VM = (props) => {

    const [width, setWidth] = useState(window.innerWidth);
    const [height, setHeight] = useState(window.innerHeight);
    const [portraitOrientation, setPortraitOrientation] = useState(false)
    const updateDimensions = () => {
        setWidth(window.innerWidth);
        setHeight(window.innerHeight);
    }
    useEffect(() => {
        window.addEventListener("resize", updateDimensions);
        return () => window.removeEventListener("resize", updateDimensions);
    }, []);

    useEffect(() => {
        {
            if (height > width) {
                setPortraitOrientation(true)
            } else {
                setPortraitOrientation(false)
            }
        }
    }, [height, width])


    setTextureStyle()


    return (
        <Box sx={{
            justifyContent: 'center',
            display: 'flex',
            alignItems: 'center',
            width: '100%',
            height: "100%",
            fontFamily: 'Roboto',
            "&::before": {
                content: '""',
                position: 'absolute',
                zIndex: 1,
                top: 0,
                left: 0,
                display: 'block',
                width: '100%',
                height: '100%',
                pointerEvents: 'none',
                backgroundImage: '',
                backgroundSize: '260px',
                opacity: 0,
            }
        }}>


            {portraitOrientation ? <MenuMobile/>:<MenuDesktop/>}

        </Box>


    )
}

export {VM}