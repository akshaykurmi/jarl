import gym

from examples.cartpole.core import PolicyNetwork, ValueFunctionNetwork, get_output_dirs, parse_args, evaluate_policy
from rl.agents.ppo.ppo_clip import PPOClip

if __name__ == '__main__':
    args = parse_args()
    ckpt_dir, log_dir = get_output_dirs('ppo_clip', args.mode == 'train')

    agent = PPOClip(
        env=gym.make('CartPole-v0'),
        policy_fn=PolicyNetwork,
        vf_fn=ValueFunctionNetwork,
        lr_policy=1e-3,
        lr_vf=1e-3,
        gamma=0.98,
        lambda_=0.96,
        delta=0.001,
        epsilon=0.05,
        epochs=150,
        episodes_per_epoch=8,
        max_episode_length=250,
        vf_update_iterations=20,
        policy_update_iterations=5,
        policy_update_batch_size=64,
        ckpt_epochs=10,
        log_epochs=1,
        ckpt_dir=ckpt_dir,
        log_dir=log_dir
    )

    if args.mode == 'train':
        agent.train()
    if args.mode == 'evaluate':
        evaluate_policy(agent.env, agent.policy)
