import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import {Paper, TextField, Typography} from "@mui/material";
import {Outlet, useParams} from "react-router-dom";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import dataPost from "../../components/utils/dataPost";

function CreateCommentPage(props) {
    let {exposition_id} = useParams();
    const [author, setAuthor] = useState('')
    const [content, setContent] = useState('')
    const [exposition, setExposition] = useState(Number(exposition_id))
    const [status, setStatus] = useState(false)
    const [validation, setValidation] = useState(false)

    function sendComment() {
        let data = {'author': author, 'content': content, 'exposition': exposition}
        dataPost(`${process.env.REACT_APP_HOST_NAME}/frontend/api/exposition/comment/`, null, data, (result) => {
            if (result['status'] === 'sanded') {
                setStatus(true)
            }
        })
    }

    useEffect(() => {
        if (author !== '' && content !== '') {
            setValidation(true)
        }
    }, [author, content])


    return (


        <Container sx={{
            fontFamily: 'Roboto',
            mt: '20px',
            justifyContent: 'center',
            display: 'grid',
            width: [300, 500]
        }}>

            <Box sx={{width: [300, 500]}}>
                <Typography variant={"h6"}>
                    {status ?
                        'Благодарим за отзыв!' :
                        'Будем благодарны за отзыв о выставке'}

                </Typography>
            </Box>
            {status ? <Box>

            </Box> : <Box sx={{display: 'grid', width: [300, 500]}}>

                <TextField required id="author" label="Имя" variant="standard"
                           sx={{width: [300, 500], marginBottom: 4}} margin="normal"
                           onChange={(e) => setAuthor(e.target.value)}
                />
                <TextField
                    required
                    sx={{width: [300, 500], marginBottom: 4}}
                    id="comment"
                    label="Текст"
                    multiline
                    maxRows={50}
                    variant="standard"
                    onChange={(e) => setContent(e.target.value)}
                />

                <Box sx={{display: "grid", justifyContent: 'right'}}>
                    <Button variant="contained" onClick={sendComment} disabled={!validation} sx={{
                        backgroundColor: 'rgb(128,110,110)',
                        width: [100, 150]
                    }}>Отправить</Button>

                </Box>


            </Box>}


        </Container>

    )
}

export {CreateCommentPage}
