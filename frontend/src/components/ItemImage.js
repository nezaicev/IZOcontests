import {styled} from "@mui/material/styles";
import IconButton from "@material-ui/core/IconButton";
import * as React from "react";
import Box from "@material-ui/core/Box";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Collapse from "@mui/material/Collapse";
import CardContent from "@material-ui/core/CardContent";
import {
    DividerStyled,
    ImageButton,
    ImageListStyled,
    TypographyStyled
} from "../styled";
import ImageGallery from "./ImageGallery";
import Typography from "@material-ui/core/Typography";
import FieldTitle from "./FieldTitle";
import formattingName from "../utils";
import PlayerModal from "./PlayerModal";
import OndemandVideoIcon from "@mui/icons-material/OndemandVideo";
import Tooltip from "@material-ui/core/Tooltip";
import CameraIcon from '@mui/icons-material/Camera';
import PictureAsPdfIcon from '@mui/icons-material/PictureAsPdf';
import ArticleIcon from '@mui/icons-material/Article';





export function ItemImage(props) {

const image=props.image

    return (<React.Fragment>


               <ImageButton sx={{
                    p: '10px',
                    margin: '10px',
                    backgroundColor: '#ffffff'
                }}
                             key={props.index}
                             ref={(props.lastElementRef) ? props.lastElementRef : undefined}
                >

                    <Box component='div' key={props.index}>
                        <a href={image['md_thumb']}>
                            <img
                                src={image['thumb']}
                                alt={props.label}
                                loading="lazy"

                            />

                        </a>
                    </Box>


                </ImageButton>




        </React.Fragment>
    )


}