import {styled} from "@mui/material/styles";
import ImageList from "@mui/material/ImageList";
import Button from "@mui/material/Button";
import {Typography} from "@mui/material";
import ImageListItem, {imageListItemClasses} from "@mui/material/ImageListItem";
import Divider from "@mui/material/Divider";



export const optionsSRLWrapper = {
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







export const DividerStyled=styled(Divider)(()=>({
    backgroundColor:'#efece3',
    height:'2px',
    border:'none',
}))
export const ImageListStyled=styled(ImageList)(()=>({

}))

export const TypographyStyled=styled(Typography)(()=>({
    display:"flex",
    fontSize:"0.975rem",
    justifyContent:"center",
    margin: '20px',
    textTransform: 'uppercase'
}))

export const ImageListItemStyled=styled(ImageListItem)(()=>({
    '&:hover': {
        backgroundColor: "#f3e3e3",
    },
    p: '10px',
    backgroundColor: '#ffffff',
    width:'280px',

}))


export const ImageButton = styled(Button)(() => ({
    '&:hover': {
        backgroundColor: "#f3e3e3",
    },
    p: '10px',
    backgroundColor: '#ffffff',


}))