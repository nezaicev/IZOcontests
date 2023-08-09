import * as React from "react";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import ReactPlayer from "react-player/youtube"
import IconButton from "@mui/material/IconButton";
import {Cancel} from "@mui/icons-material";
import ImageListItemBar from "@mui/material/ImageListItemBar";
import ImageListItem from "@mui/material/ImageListItem";
import {styled} from '@mui/material/styles';
import Tooltip from "@mui/material/Tooltip";
import Card from "@mui/material/Card";
import OndemandVideoIcon from '@mui/icons-material/OndemandVideo';

import {
    getThumbYoutube,
    deleteYoutubeLogo,
    getFormattedDate
} from "../utils/utils";
import Typography from "@mui/material/Typography";

const CardVideo = styled(Card)(() => ({

    "& .MuiPaper-elevation1": {boxShadow: '0'},
    alignItems: 'baseline',
    flexDirection: 'column',
    margin: '15px',
    width: '340px',
    height: 'fit-content'
}))


export default function VideoItem(props) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {
        setOpen(true)
    };
    const handleClose = () => setOpen(false);
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    return (

        <Box>


            {/*<CardVideo sx={{boxShadow: '0'}} ref={props.forwardedRef}>*/}
            <CardVideo sx={{boxShadow: '0'}}>
                <Box sx={{
                    p: '10px',
                    backgroundColor: '#ffffff'
                }} onClick={handleOpen}>

                    <ImageListItem>

                        <Box>
                            <a href='#'>
                                <img
                                    src={getThumbYoutube(props.link, 'mqdefault')}
                                    alt={props.title}
                                    loading="lazy"/>
                            </a>


                            <ImageListItemBar
                                sx={{
                                    backgroundColor: "rgb(129 110 110 / 76%)"
                                }}
                                title={props.title}
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

                <Box>

                    <Box sx={{
                        paddingLeft: '10px',
                        paddingRight: '10px',
                        paddingBottom: '10px',
                        alignContent: 'center'
                    }}>
                        <Typography>{props.description ? props.description : props.title}</Typography>
                    </Box>

                </Box>

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
                            url={props.link}
                        >
                        </ReactPlayer>
                    </div>


                </Box>


            </Modal>


        </Box>

    );
}
