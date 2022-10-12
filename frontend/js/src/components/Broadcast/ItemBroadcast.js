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

const style = {

    position: 'absolute',
    top: '70%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    height: [400],
    width: [400],
    textAlign: 'center',

};

const ItemBarBroadcast = styled(ImageListItemBar)(({theme}) => ({
    backgroundColor: "rgb(129 110 110 / 76%)",

    "& .MuiImageListItemBar-title": {
        fontSize: '14px'
    }

}));
const CardBroadcast = styled(Card)(() => ({

    "& .MuiPaper-elevation1": {boxShadow: '0'},
    alignItems: 'baseline',
    flexDirection: 'column',
    margin: '20px',
    width: '340px',
    height: 'fit-content'
}))



export default function ItemBroadcast(props) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {setOpen(true)};
    const handleClose = () => setOpen(false);
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    return (

        <Box>


            <CardBroadcast sx={{boxShadow: '0'}} ref={props.forwardedRef}>
                <Box sx={{
                    p: '10px',
                    backgroundColor: '#ffffff'
                }} onClick={handleOpen}>

                    <ImageListItem>

                        <Box>
                            <a href='#'>
                                <img
                                    src={getThumbYoutube(props.data['broadcast_url'], 'mqdefault')}
                                    alt={props.data['name']}
                                    loading="lazy"/>
                            </a>


                            <ImageListItemBar
                                sx={{
                                    backgroundColor: "rgb(129 110 110 / 76%)"
                                }}
                                title={getFormattedDate(props.data['start_date'])}
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
                {props.data ?
                    <Box>

                        <Box sx={{paddingLeft: '10px',paddingRight: '10px',paddingBottom: '10px', alignContent:'center'}}>
                            {/*<Box sx={{ display: expanded ? 'none' : 'block'}}>*/}

                           <Typography>{props.data['name']}</Typography>
                                {/*</Box>*/}
                            {/*<Box sx={{*/}
                            {/*    textAlign: 'right',*/}
                            {/*    marginRight: '-10px',*/}
                            {/*    marginBottom: '-10px'*/}
                            {/*}}>*/}
                                {/*<ButtonCollapse*/}
                                {/*    expand={expanded}*/}
                                {/*    onClick={handleExpandClick}*/}
                                {/*    aria-expanded={expanded}*/}
                                {/*    aria-label="show more"*/}
                                {/*    sx={{p: '2px'}}>*/}
                                {/*    <ExpandMoreIcon/>*/}
                                {/*</ButtonCollapse>*/}
                            {/*</Box>*/}

                        </Box>
                        {/*<Collapse in={expanded} timeout="auto" unmountOnExit>*/}
                        {/*    <CardContent sx={{padding:'8px'}}>*/}
                        {/*     <p> Test</p>*/}
                        {/*    </CardContent>*/}
                        {/*</Collapse>*/}
                    </Box> : ''}
            </CardBroadcast>


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
                            url={props.data['broadcast_url']}
                        >
                        </ReactPlayer>
                    </div>


                </Box>


            </Modal>


        </Box>

    );
}
