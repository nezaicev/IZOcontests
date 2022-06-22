import * as React from "react";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import ReactPlayer from "react-player"
import IconButton from "@mui/material/IconButton";
import {Cancel} from "@mui/icons-material";
import ImageListItemBar from "@mui/material/ImageListItemBar";
import ImageListItem from "@mui/material/ImageListItem";
import {styled} from '@mui/material/styles';
import Tooltip from "@mui/material/Tooltip";
import Collapse from '@mui/material/Collapse';
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import CardContent from "@mui/material/CardContent";
import Card from "@mui/material/Card";
import OndemandVideoIcon from '@mui/icons-material/OndemandVideo';
import {ImageButton} from "../styled";
import {ItemVisibleVP} from "./VP/ItemVisibleVP";

const style = {

    position: 'absolute',
    top: '70%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    height: [400],
    width: [400],
    textAlign: 'center',

};

const CustomItemBar = styled(ImageListItemBar)(({theme}) => ({
    backgroundColor: "rgb(129 110 110 / 76%)",

    "& .MuiImageListItemBar-title": {
        fontSize: '14px'
    }

}));
const CardVideo = styled(Card)(() => ({

    "& .MuiPaper-elevation1": {boxShadow: '0'},
    alignItems: 'baseline',
    flexDirection: 'column',
    margin: '20px',
    width: '340px',
    height: 'fit-content'
}))


function getThumbYoutube(url, quality) {
    let thumbUrl;
    let idVideo = new URL(url)
    idVideo = idVideo.pathname.substr(1, 12).split('&').join('')
    thumbUrl = `http://img.youtube.com/vi/${idVideo}/${quality}.jpg`;
    return thumbUrl
}

export default function VideoItem(props) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    return (

        <Box>


            <CardVideo sx={{boxShadow: '0'}} ref={props.forwardedRef}>
                <Box sx={{
                    p: '10px',
                    backgroundColor: '#ffffff'
                }} onClick={handleOpen}>

                    <ImageListItem>

                        <Box>
                            <a href='#'>
                                <img
                                    src={getThumbYoutube(props.url, 'mqdefault')}
                                    alt={props.name}
                                    loading="lazy"/>
                            </a>


                            <ImageListItemBar
                                sx={{
                                    backgroundColor: "rgb(129 110 110 / 76%)"
                                }}
                                title={props.name.toUpperCase()}
                                actionIcon={
                                    <Tooltip title="Видео">
                                        <IconButton>
                                            <OndemandVideoIcon sx={{
                                                color: "#fff",
                                                p: '5px'
                                            }}/>
                                        </IconButton>
                                    </Tooltip>
                                }
                            >

                            </ImageListItemBar>


                        </Box>

                    </ImageListItem>

                </Box>
                {/*<ItemVisibleVP*/}
                {/*    expand={expanded}*/}
                {/*    onClick={handleExpandClick}*/}
                {/*    aria-expanded={expanded}*/}
                {/*    aria-label="show more"*/}
                {/*    sx={{p: '2px'}}*/}
                {/*>*/}
                {/*    <ExpandMoreIcon/>*/}
                {/*</ItemVisibleVP>*/}
                {/*<Collapse in={expanded} timeout="auto" unmountOnExit>*/}
                {/*    <CardContent>*/}
                {/*        <Typography>*/}
                {/*            {props.name}*/}
                {/*        </Typography>*/}

                {/*    </CardContent>*/}
                {/*</Collapse>*/}
            </CardVideo>


            <Modal
                open={open}
                onClose={handleClose}
                sx={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignContent: 'center',
                    alignItems: 'center'
                }}
            >

                <Box sx={{width: [400, 500, 600, 800]}}>
                    <Box sx={{textAlign: 'right'}} component='div'>
                        <IconButton aria-label="Cancel" onClick={handleClose}>
                            <Cancel sx={{color: '#ffffff'}}/>

                        </IconButton>
                    </Box>
                    <div className='player-wrapper'>


                        <ReactPlayer
                            className='react-player'
                            width='100%'
                            height='100%'
                            controls={true}
                            url={props.url}
                        >
                        </ReactPlayer>
                    </div>


                </Box>


            </Modal>


        </Box>

    );
}
