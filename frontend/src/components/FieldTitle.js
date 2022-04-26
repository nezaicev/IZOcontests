import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import * as React from "react";


export default function FieldTitle(props) {
    if (props.content) {
        return (
            <Box>
                <Typography variant='subtitle2' component={'span'}>
                    {props.title}
                </Typography>
                <Typography variant='body2' component={'span'}>
                    {props.content}
                </Typography>
            </Box>

        )
    }
    else{
        return (<></>)
    }


}