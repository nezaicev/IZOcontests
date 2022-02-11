import * as React from "react";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import ReactPlayer from "react-player";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import {Cancel} from "@mui/icons-material";
import ImageListItemBar from "@material-ui/core/ImageListItemBar";

import ImageListItem from "@material-ui/core/ImageListItem";
import {styled} from '@mui/material/styles';
import Tooltip from "@material-ui/core/Tooltip";
import Collapse from '@mui/material/Collapse';
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import CardContent from "@material-ui/core/CardContent";
import Card from "@material-ui/core/Card";
import OndemandVideoIcon from '@mui/icons-material/OndemandVideo';

const style = {

    position: 'absolute',
    top: '45%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: [480, 680],
    height: [170, 300, 400],
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

const ImageButton = styled(Button)(() => ({
    '&:hover': {
        backgroundColor: "#f3e3e3",
    },

}))

const ExpandMore = styled((props) => {
    const {expand, ...other} = props;
    return <IconButton {...other} />;
})(({theme, expand}) => ({
    display: 'inline-flex',
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
        duration: theme.transitions.duration.shortest,
    }),
}));


function getThumbYoutube(url, quality) {
    let thumbUrl;
    let idVideo = new URL(url)
    idVideo = idVideo.pathname.substr(1, 12).split('&').join('')
    thumbUrl = `http://img.youtube.com/vi/${idVideo}/${quality}.jpg`;
    return thumbUrl
}

export default function PlayerModal(props) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    return (


        <React.Fragment>


            <CardVideo sx={{boxShadow: '0'}}>
                <ImageButton sx={{p: '10px', backgroundColor: '#ffffff'}} onClick={handleOpen}>

                    <ImageListItem>
                        <Box>
                            <img src={getThumbYoutube(props.url, 'mqdefault')}
                                 alt={props.name}
                                 loading="lazy"/>

                            <CustomItemBar
                                title={props.name}
                                position={'bottom'}
                                actionIcon={
                                    <Tooltip title="Видео">
                                        <IconButton>
                                            <OndemandVideoIcon sx={{color: "#fff", p: '5px'}}/>
                                        </IconButton>
                                    </Tooltip>
                                }
                            >

                            </CustomItemBar>


                        </Box>
                    </ImageListItem>

                </ImageButton>
                <ExpandMore
                    expand={expanded}
                    onClick={handleExpandClick}
                    aria-expanded={expanded}
                    aria-label="show more"
                    sx={{p: '5px'}}
                >
                    <ExpandMoreIcon/>
                </ExpandMore>
                <Collapse in={expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                        <Typography>
                            {props.name}
                        </Typography>

                    </CardContent>
                </Collapse>
            </CardVideo>

            <Modal
                open={open}
                onClose={handleClose}
            >

                <Box sx={style}>
                    <Box sx={{textAlign: 'right', width: [700, 700]}}>
                        <IconButton aria-label="Cancel" onClick={handleClose}>
                            <Cancel sx={{color: '#eae0a4'}}/>

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


        </React.Fragment>

    );
}
