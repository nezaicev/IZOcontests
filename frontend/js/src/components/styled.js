import {styled} from "@mui/material/styles";
import ImageList from "@mui/material/ImageList";
import Button from "@mui/material/Button";
import {createTheme, Typography} from "@mui/material";
import ImageListItem, {imageListItemClasses} from "@mui/material/ImageListItem";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import * as React from "react";
import {brown} from "@mui/material/colors";



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

export const ButtonCollapse = styled((props) => {
    const {expand, ...other} = props;
    return <IconButton {...other} />;
})(({theme, expand}) => ({
    backgroundColor: 'rgb(239, 236, 227)',
    '&:hover': {
        backgroundColor: "#c4b7b7",
    },
    margin: '5px',
    display: 'inline-flex',
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',

    transition: theme.transitions.create('transform', {
        duration: theme.transitions.duration.shortest,
    }),
}));

export  const customThemeTab = createTheme({
  components:{
      MuiButtonBase:{
          styleOverrides:{
              root:
                  {height:'60px'},

          }
      }
  }
});

export const ButtonDefault = styled(Button)(({ theme }) => ({
  color: theme.palette.getContrastText(brown[100]),
  backgroundColor: brown[100],
    border:brown[200],
  '&:hover': {
    backgroundColor: brown[200],
      border:brown[200],
  },
}));