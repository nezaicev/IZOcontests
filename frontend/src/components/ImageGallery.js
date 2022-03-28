import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import ImageListItem from "@material-ui/core/ImageListItem";
import React from "react";
import {ImageListStyled} from "../styled";

import Box from "@material-ui/core/Box";



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
        overlayColor: 'rgb(104 99 97 / 98%)',
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

                <ImageListStyled sx={{justifyContent:'space-around'}} cols={[]} rowHeight={250} >
                    {images.map((item,index) => (
                        <Box sx={{
                            padding: '10px',
                            margin: '10px',
                            marginTop:'20px',
                            width:[250,300],
                            height:[250,250]
                        }} elevation={3}>
                            <ImageListItem  key={index}>
                                <a href={item['original']}>
                                    <img
                                        src={item['thumb']}
                                        alt={title}
                                        loading="lazy"

                                    />

                                </a>
                            </ImageListItem>
                        </Box>

                    ))}
                </ImageListStyled>
                </Box>


            </SRLWrapper>
        </SimpleReactLightbox>)
}