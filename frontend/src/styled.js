import {styled} from "@mui/material/styles";
import ImageList from "@mui/material/ImageList";
import Button from "@mui/material/Button";
import {Typography} from "@mui/material";
import ImageListItem, {imageListItemClasses} from "@mui/material/ImageListItem";
import Divider from "@mui/material/Divider";


export const DividerStyled=styled(Divider)(()=>({
    backgroundColor:'#efece3',
    height:'2px'
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