/**
 * Created by vlad on 22.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';

class GetMembersSubscriptions extends React.Component {
    method_name = 'Collector.Groups.get_members_subscriptions';
    default_state = {
        group_id: '',
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
        this.setState({group_id: event.target.value});
    }

    handleLimitChange(event) {
        this.setState({limit: event.target.value});
    }

    handleSubmit(event) {
        send_task(this.method_name, {
            'group_id': this.state.group_id,
            'limit': this.state.limit
        });
        this.setState(this.default_state);
        event.preventDefault();
    }


    render() {
        return (
            <div class='content'>
                <div className="page-header">
                    <h1>Сбор пользователей, на которых подписаны подписчики сообщества</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите ссылку на сообщество:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.group_id}
                            placeholder="coffman"
                            onChange={this.handleChange}
                        />
                        <ControlLabel>У какого кол-ва подписчиков пользователь должен быть в подписках:</ControlLabel>
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
;

export default GetMembersSubscriptions
