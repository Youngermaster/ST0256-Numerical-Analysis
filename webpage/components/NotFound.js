import React from "react";
import {generatePath} from "./utils";
import { Link } from "react-router-dom";
import Button from '@material-ui/core/Button';
import HomeIcon from '@material-ui/icons/Home';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Slide from '@material-ui/core/Slide';
import haroldImage from '../images/harold.jpg';
import { Zoom } from "react-awesome-reveal";

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

function NotFound() {
    return (
        <Dialog
            open={true}
            disableBackdropClick={true}
            disableEscapeKeyDown={true}
            TransitionComponent={Transition}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
        >
            <DialogTitle id="alert-dialog-title">Page not found!</DialogTitle>
            <DialogContent>
            <DialogContentText id="alert-dialog-description">
                Seems the specified URL does not link to any valid part of the website.
            </DialogContentText>
            <Zoom duration={500} triggerOnce cascade>
                <img width="100%" height="auto" src={haroldImage} alt="Hide the Pain Harold" />
                <DialogActions>
                    <Button component={Link} to={generatePath()} variant="contained" color="primary" endIcon={<HomeIcon/>}>
                        Go to Main Menu
                    </Button>
                </DialogActions>
            </Zoom>
            </DialogContent>
        </Dialog>
    );
}

export default NotFound;