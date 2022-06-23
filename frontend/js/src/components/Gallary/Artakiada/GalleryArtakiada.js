import VerticalTabs from "../VerticalTabs";
import HorizontalTabs from "../HorizontalTabs";
import React, {useEffect, useState} from "react";
import VisibleBox from "../VisibleBox";
import {Box} from "@mui/material";
import dataFetch from "../../utils/dataFetch";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {optionsSRLWrapper} from "../../styled";
import ImageListItem from "@mui/material/ImageListItem";


export default function GalleryArtakiada(props) {
    const [dataVerticalTabs, setDataVerticalTabs] = React.useState([])
    const [valueVerticalTabs, setValueVerticalTabs] = React.useState('')
    const [dataHorizontalTabs, setDataHorizontalTabs] = React.useState([])
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const [params, setParams] = React.useState({contest_name: props.contestName})
    const [page, setPage] = useState(1)


    useEffect(() => {
        dataFetch(props.urlVerticalTabs, params, (data) => {
            setDataVerticalTabs(data, [setValueVerticalTabs(0)]);
        })
    }, [])

    useEffect(() => {
        params['year_contest'] = dataVerticalTabs[valueVerticalTabs]
        dataFetch(props.urlHorizontalTabs, params, (data) => {
            setDataHorizontalTabs(data, [setValueHorizontalTabs(0)])
        })
    }, [valueVerticalTabs])


    const visualComponent = (items, ref) => {

        return (

            <SimpleReactLightbox>
                <SRLWrapper options={optionsSRLWrapper}>
                    <Box sx={{
                        display: 'grid',
                        gridTemplateColumns: `repeat(auto-fill, minmax(300px, 1fr))`,
                        justifyItems: 'center',
                        alignItems: 'center',
                        marginBottom: '30px',

                    }}>

                        {items.images.map((item, index) => (

                            <ImageListItem key={index} sx={{marginTop: '25px'}}
                            >

                                <a href={item['md_thumb']}>
                                    <img
                                        src={item['thumb']}
                                        alt={title}
                                        loading="lazy"
                                    />

                                </a>
                            </ImageListItem>


                        ))}

                    </Box>


                </SRLWrapper>
            </SimpleReactLightbox>
        )


    }


    return (<React.Fragment>
            <Box sx={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                alignItems: 'center'
            }}>

                <HorizontalTabs contestName={props.contestName}
                                data={dataHorizontalTabs}
                                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue), [setPage(1)]))}
                                valueVerticalTabs={valueVerticalTabs}
                />

                <VerticalTabs contestName={props.contestName}
                              data={dataVerticalTabs}
                              setValueVerticalTabs={(newValue) => (setValueVerticalTabs(newValue, [setPage(1)]))}

                />
            </Box>
            <Box sx={{}}>

                <VisibleBox
                    visualComponent={visualComponent}
                    url={props.urlContent}
                    contestName={props.contestName}
                    year={dataVerticalTabs[valueVerticalTabs]}
                    nomination={dataHorizontalTabs[valueHorizontalTabs]}
                    page={page}
                    setPage={(newValue) => {
                        setPage(newValue)
                    }}
                />

            </Box>
        </React.Fragment>
    )
}