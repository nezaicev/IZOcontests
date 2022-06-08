import Card from "@mui/material/Card";



import React, {useEffect, useState} from "react";
import {styled} from "@mui/material/styles";
import useInfiniteScroll from "../useInfiniteScroll";
import axios from "axios";
import Box from "@mui/material/Box";
import CircularProgress from "@mui/material/CircularProgress";
import {ExpandMoreCollapse} from "./ExpandMore";
import HorizontalTabs from "./HorizontalTabs";
import VerticalTabs from "./VerticalTabs";


const MixCard = styled(Card)(() => ({
    justifyContent: 'center',
    alignItems: 'baseline',
    flexDirection: 'column',
    margin: '20px',
    marginTop: '30px',
    padding: '20px',
    height: 'fit-content',
    boxShadow: 0
}))


export default function VPGallery(props) {
    const hostName = process.env.REACT_APP_HOST_NAME
    const contestNameVP = process.env.REACT_APP_VP
    const [Items, setItems] = useState([]);
    const [isFetching, setIsFetching] = useState(false);
    const [page, setPage] = useState(1);
    const [nomination, setNomination] = useState('');
    const [nominations, setNominations] = useState([]);
    const [year, setYear] = useState('');
    const [HasMore, setHasMore] = useState(true);

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );

    const resetPage = () => {
        setPage((value) => {
            return 1
        });

    }


    function loadMoreItems() {
        setIsFetching(true);

        axios({
            method: "GET",
            url: `http://${hostName}/frontend/api/archive/`,
            params: {
                page_size: 1,
                publish: true,
                contest_name: props.contestName,
                year:year,
                page: page,
                nomination: (nomination === 'Все') ? '' : nomination,
                ordering: '-rating',
            },
        })
            .then((res) => {
                setItems((prevTitles) => {
                    return [...new Set([...prevTitles, ...res.data.results.map((b) => b)])];
                });
                setPage((prevPageNumber) => prevPageNumber + 1);
                setHasMore(!!res.data.next);
                setIsFetching(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }


    return (
        <Box sx={{justifyContent: 'center'}}>
            <Box sx={{
                margin: '20px',
                width: 'auto',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
            }}>
                <HorizontalTabs
                    url={`http://${hostName}/frontend/api/contest/nominations?contest_name=${contestNameVP}&year_contest=${year}`}
                    loadData={loadMoreItems}
                    nominations={nominations}
                    resetPage={resetPage}
                    resetLoadedData={() => {
                        setItems([]);
                    }}
                    setNomination={(value) => {
                        setNomination(value);
                    }}
                />

                <VerticalTabs
                    url={`http://${hostName}/frontend/api/archive/contest/years?contest_name=${contestNameVP}`}
                    resetPage={resetPage}
                    resetNominations={

                    }

                    setYear={(value) => {
                        setYear(value);
                    }}
                    resetLoadedData={() => {
                        setItems([]);
                    }}
                />
            </Box>

            {Items.map((item, index) => {
                if (Items.length === index + 1) {

                    return (
                        <MixCard sx={{boxShadow: '0', padding: '0px'}}
                                 key={index}>


                            <ExpandMoreCollapse item={item} index={index}
                                                lastElementRef={lastElementRef}/>


                        </MixCard>

                    );
                } else {
                    return (<MixCard sx={{boxShadow: '0', padding: '0px'}}
                                     key={index}>


                            <ExpandMoreCollapse item={item} index={index}/>


                        </MixCard>

                    )


                }
            })}
            {isFetching && <Box sx={{
                justifyContent: 'center',
                height: '600',
                display: 'flex'
            }}>
                <CircularProgress/>
            </Box>}
        </Box>
    )
}