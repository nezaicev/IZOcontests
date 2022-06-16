import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import ImageListItem from "@mui/material/ImageListItem";
import React from "react";
import {ImageListStyled} from "../styled";

import Box from "@mui/material/Box";
import ImageList from "@mui/material/ImageList";


const options = {
    settings: {
        autoplaySpeed: 3000,
        boxShadow: 'none',
        disableKeyboardControls: false,
        disablePanzoom: false,
        disableWheelControls: false,
        hideControlsAfter: false,
        lightboxTransitionSpeed: 0.3,
        lightboxTransitionTimingFunction: 'linear',
        overlayColor: 'rgb(38 30 27 /98%)',
        slideAnimationType: 'fade',
        slideSpringValues: [300, 50],
        slideTransitionSpeed: 0.6,
        slideTransitionTimingFunction: 'linear',
        usingPreact: false
    },
    buttons: {
        backgroundColor: "rgb(104 99 97)",
        iconColor: "#dcd9d9",
    },
    caption: {
        captionColor: "#ffffff",
        fontFamily: "Roboto",
        captionContainerPadding: '0px 0 0px 0',
        showCaption: true

    },
    thumbnails: {
        showThumbnails: false
    }

};


export default function ImageGallery(props) {
    const images = props.images
    const title = props.titleImg
    return (
        <SimpleReactLightbox>
            <SRLWrapper options={options}>
                <Box>

                    <ImageList sx={{
                        display: "flex",
                        justifyItems:"center",
                        alignItems: "center",
                        justifyContent:"space-evenly",
                        alignContent:"space-evenly",
                        marginLeft: "auto",
                        marginLight: "auto",
                        gridTemplateColumns: "100px 100px 100px",
                        gridTemplateRows: "auto",
                    }} cols={3} rowHeight={180}>
                        {images.map((item, index) => (

                            <ImageListItem key={index}>
                                <a href={item['md_thumb']}>
                                    <img
                                        src={item['thumb']}
                                        alt={title}
                                        loading="lazy"
                                    />

                                </a>
                            </ImageListItem>


                        ))}
                    </ImageList>
                </Box>


            </SRLWrapper>
        </SimpleReactLightbox>)
}