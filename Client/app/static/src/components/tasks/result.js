/**
 * Created by vlad on 22.11.16.
 */

var React = require('react');
import {get_result_list} from '../../api/task'
import Media from 'react-bootstrap/lib/Media';
import Image from 'react-bootstrap/lib/Image';
import ListGroup from 'react-bootstrap/lib/ListGroup';
import ListGroupItem from 'react-bootstrap/lib/ListGroupItem';


class Result extends React.Component {
    constructor(props) {
        super(props);
    }

    userView = (
        <div>
            <Media>
                <Media.Left>
                    <a href={"http://vk.com/id"+this.props.data.uid}>
                        <Image width={64} height={64}
                             src={this.props.data.photo ? this.props.data.photo:'http://vk.com/images/camera_b.gif'}
                             alt="Image" circle/></a>
                </Media.Left>
                <Media.Body>
                    <Media.Heading>
                        <a href={"http://vk.com/id"+this.props.data.uid}>
                            {this.props.data.first_name + ' ' + this.props.data.last_name}
                        </a>
                    </Media.Heading>
                    <div>
                        <ListGroup>
                            {this.props.data.values.map(function (value) {
                                    return (
                                        <ListGroupItem>
                                            <b>{value.name + ': '}</b>
                                            <i>{value.value}</i>
                                        </ListGroupItem>
                                    )
                                }
                            )
                            }
                        </ListGroup>
                    </div>
                </Media.Body>
            </Media>
        </div>
    );

    groupView = (
        <div>
            <Media>
                <Media.Left>
                    <a href={"http://vk.com/club"+this.props.data.gid}>
                        <Image width={64} height={64}
                             src={this.props.data.photo ? this.props.data.photo:'http://vk.com/images/camera_b.gif'}
                             alt="Image" circle/></a>
                </Media.Left>
                <Media.Body>
                    <Media.Heading>
                        <a href={"http://vk.com/club"+this.props.data.gid}>
                            {this.props.data.name}
                        </a>
                    </Media.Heading>
                    <div>
                        <ListGroup>
                            {this.props.data.values.map(function (value) {
                                    return (
                                        <ListGroupItem>
                                            <b>{value.name + ': '}</b>
                                            <i>{value.value}</i>
                                        </ListGroupItem>
                                    )
                                }
                            )
                            }
                        </ListGroup>
                    </div>
                </Media.Body>
            </Media>
        </div>
    );

    valuesView = (
        <ListGroup>
            {this.props.data.values.map(function (value) {
                    return (
                        <ListGroupItem>
                            <b>{value.name + ': '}</b>
                            <i>{value.value}</i>
                        </ListGroupItem>
                    )
                }
            )
            }
        </ListGroup>
    );

    render() {
        switch (this.props.data.type) {
            case 'user':
                return this.userView;
            case 'group':
                return this.groupView;
            default:
                return this.valuesView
        }
    }
}

export default Result
