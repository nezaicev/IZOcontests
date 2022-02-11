import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import ImageList from "@material-ui/core/ImageList";
import ImageListItem from "@material-ui/core/ImageListItem";
import React from "react";


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
        overlayColor: 'rgba(71,52,52,0.9)',
        slideAnimationType: 'fade',
        slideSpringValues: [300, 50],
        slideTransitionSpeed: 0.6,
        slideTransitionTimingFunction: 'linear',
        usingPreact: false
    },
    buttons: {
        backgroundColor: "#523232",
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
    return (
        <SimpleReactLightbox >
            <SRLWrapper options={options}>
                <ImageList sx={{width: 300, height: 300}} cols={4} rowHeight={250}>
                    {images.map((item) => (
                        <ImageListItem key={item.url}>

                            <img
                                src={item.url}
                                alt={item.name}
                                loading="lazy"

                            />


                        </ImageListItem>
                    ))}
                </ImageList>

            </SRLWrapper>
        </SimpleReactLightbox>)
}