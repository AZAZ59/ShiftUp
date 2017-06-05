/**
 * Created by vlad on 22.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';

class GetFriends extends React.Component {
    method_name = 'Collector.Users.get_friends';
    default_state = {
        user_ids: '',
        limit: 2
    };

    constructor(props) {
        super(props);
        this.state = this.default_state;

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleLimitChange = this.handleLimitChange.bind(this);
    }

    handleChange(event) {
        this.setState({user_ids: event.target.value});
    }

    handleLimitChange(event) {
        this.setState({limit: event.target.value});
    }

    handleSubmit(event) {
        send_task(this.method_name, {
            'user_ids': this.state.user_ids.split(','),
            'limit': this.state.limit
        });
        this.setState(this.default_state);
        event.preventDefault();
    }


    render() {
        return (
            <div class='content'>
                <div className="page-header">
                    <h1>Сбор друзей пользователей</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите список людей через запятую:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.user_ids}
                            placeholder="durov, id1"
                            onChange={this.handleChange}
                        />
                        <ControlLabel>У какого кол-ва пользователь должен состоять в друзьях:</ControlLabel>
                        <FormControl
                            type="number"
                            value={this.state.limit}
                            placeholder="2"
                            onChange={this.handleLimitChange}
                        />
                    </FormGroup>
                    <Button type="submit">
                        Отправить
                    </Button>
                </form>
            </div>
        );
    }
}


export default GetFriends
