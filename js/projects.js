// Projects data - add your projects here
const projectsData = [
  {
    title: "Deep Learning-Based Vehicle Detection and Traffic Flow Analysis",
    date: "June 2021",
    description: "Built an end-to-end system for traffic monitoring using YOLOv4, DeepSORT tracking, and SVM classification for lane detection from aerial imagery.",
    tags: ["Python", "TensorFlow", "YOLOv4", "Computer Vision"],
    github: "https://github.com/ahmadrezafrh/Traffic-Flow-Measurement-Deep-Learning",
    report: null,
    demo: null,
    page: "projects/traffic-flow.html",
    featured: true,
    preview: "projects/traffic-flow/demo.gif"
  },
  {
    title: "Sim-to-Real Transfer of RL Policies in Robotics",
    date: "March 2023",
    description: "Trained PPO agents on the MuJoCo Hopper environment with domain randomization to bridge the sim-to-real gap. Explored vision-based RL with CNN preprocessing and MobileNetV2 feature extraction.",
    tags: ["Python", "PyTorch", "MuJoCo", "PPO", "Domain Randomization"],
    github: "https://github.com/ahmadrezafrh/Sim-to-Real-transfer-in-Reinforcement-Learning",
    report: null,
    demo: null,
    page: "projects/sim-to-real.html",
    featured: true,
    preview: "projects/sim-to-real/rgb.png"
  },
  {
    title: "Custom Gym Environment for Board Game RL with Stable Baselines3",
    date: "December 2023",
    description: "Designed a custom OpenAI Gym environment with shaped reward functions for the Quixo board game. Trained PPO, DQN, and A2C agents using Stable Baselines3 with custom MLP architectures.",
    tags: ["Python", "Reinforcement Learning", "OpenAI Gym", "Stable Baselines3"],
    github: "https://github.com/ahmadrezafrh/Quixo-Computational-Intelligence-2023-2024",
    report: null,
    demo: null,
    page: "projects/quixo-rl.html",
    featured: false,
    preview: "projects/quixo-rl/gui2.png"
  },
  {
    title: "An IoT Synthetic Data Generation Module for Capping Devices",
    date: "March 2024",
    description: "Full-stack web application for generating synthetic sensor data using Temporal Fusion Transformer. React/TypeScript frontend, Flask backend with thread pool for concurrent generation, MongoDB storage.",
    tags: ["Python", "PyTorch", "React", "Flask", "MongoDB", "TFT"],
    github: "https://github.com/ahmadrezafrh/AROL-Data-Generation-Module",
    report: null,
    demo: null,
    page: "projects/arol-data-gen.html",
    featured: true,
    preview: "projects/arol-data-gen/MinLockPosition_heads_14.png"
  },
  {
    title: "Kuka-V1 Robot Anomaly Detection Using Transformer and Graph Attention Models",
    date: "September 2023",
    description: "Unsupervised time-series anomaly detection for robotic sensor data using Anomaly Transformer. Developed a novel evaluation algorithm for contextual anomaly detection with sliding window scoring.",
    tags: ["Python", "PyTorch", "Transformers", "Anomaly Detection", "Time Series"],
    github: "https://github.com/ahmadrezafrh/Time-Series-Anomaly-Detection-SOTA-Investigation",
    report: null,
    demo: null,
    page: "projects/ts-anomaly-detection.html",
    featured: true,
    preview: "projects/ts-anomaly-detection/tempral.png"
  },
  {
    title: "RobVC: A Robust End-to-End Self-Supervised Voice Conversion",
    date: "March 2024",
    description: "Master's thesis on voice conversion using novel cross-attention mechanism for implicit speaker-content disentanglement. Achieves state-of-the-art speaker similarity using HuBERT and EnCodec pretrained models.",
    tags: ["Python", "PyTorch", "Deep Learning", "Voice Conversion", "Self-Supervised Learning"],
    github: null,
    report: "https://webthesis.biblio.polito.it/secure/35238/1/tesi.pdf",
    demo: null,
    page: "projects/robvc.html",
    featured: true,
    preview: "projects/robvc/newdes.png"
  }
];
