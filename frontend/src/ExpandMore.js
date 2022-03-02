import {styled} from "@mui/material/styles";
import IconButton from "@material-ui/core/IconButton";
import * as React from "react";

export const ExpandMore = styled((props) => {
    const {expand, ...other} = props;
    return <IconButton {...other} />;
})(({theme, expand}) => ({
    backgroundColor:'#faebd7',
    '&:hover': {
        backgroundColor: "#c4b7b7",
    },
    margin:'5px',
    display: 'inline-flex',
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
        duration: theme.transitions.duration.shortest,
    }),
}));