from typing import Union, Tuple

import torch
from torch.distributions import Normal

from . import Noise


class OrnsteinUhlenbeckNoise(Noise):
    def __init__(self, 
                 theta: float, 
                 sigma: float, 
                 base_scale: float, 
                 mean: float = 0, 
                 std: float = 1, 
                 device: Union[str, torch.device] = "cuda:0") -> None:
        """Class representing an Ornstein-Uhlenbeck noise

        :param theta: Factor to apply to current internal state
        :type theta: float
        :param sigma: Factor to apply to the normal distribution
        :type sigma: float
        :param base_scale: Factor to apply to returned noise
        :type base_scale: float
        :param mean: Mean of the normal distribution (default: 0.0)
        :type mean: float, optional
        :param std: Standard deviation of the normal distribution (default: 1.0)
        :type std: float, optional
        :param device: Device on which a torch tensor is or will be allocated (default: "cuda:0")
        :type device: str or torch.device, optional
        """
        super().__init__(device)

        self.state = 0
        self.theta = theta
        self.sigma = sigma
        self.base_scale = base_scale

        self.distribution = Normal(loc=torch.tensor(mean, device=self.device, dtype=torch.float32),
                                   scale=torch.tensor(std, device=self.device, dtype=torch.float32))
        
    def sample(self, size: Union[Tuple[int], torch.Size]) -> torch.Tensor:
        """Sample an Ornstein-Uhlenbeck noise

        :param size: Shape of the sampled tensor
        :type size: tuple or list of integers, or torch.Size
        
        :return: Sampled noise
        :rtype: torch.Tensor
        """
        if isinstance(self.state, torch.Tensor) and self.state.size() != torch.Size(size):
            self.state = 0
        self.state += -self.state * self.theta + self.sigma * self.distribution.sample(size)
        
        return self.base_scale * self.state
