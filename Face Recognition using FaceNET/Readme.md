### 1. Face Recognition using FaceNet
   Face recognition is a computer vision task of identifying and verifying a person based on a photograph of their face.
   
   <a href="https://www.pluralsight.com/guides/face-recognition-walkthrough-facenet" target="blank"><img align="center" src="https://arsfutura-production.s3.amazonaws.com/blog_posts/og_images/000/000/008/original/08-face-recognition-og-image.png?1614777174" alt="@waghhimanshu" height="250" width="550" /></a>   
   
   ### FaceNet Model
   FaceNet is a face recognition system that was described by Florian Schroff, et al. at Google in their 2015 paper titled “FaceNet: A Unified Embedding for Face Recognition and Clustering.”

   It is a system that, given a picture of a face, will extract high-quality features from the face and predict a 128 element vector representation these features, called a face embedding.

   FaceNet, that directly learns a mapping from face images to a compact Euclidean space where distances directly correspond to a measure of face similarity.
   
   ### How does Facenet work?
   
   <a href="https://www.pluralsight.com/guides/face-recognition-walkthrough-facenet" target="blank"><img align="center" src="https://miro.medium.com/max/1400/1*ZD-mw2aUQfFwCLS3cV2rGA.png" alt="@waghhimanshu" height="200" width="650" /></a> 
   
   Facenet uses convolutional layers to learn representations directly from the pixels of the face. This network was trained on a large dataset to achieve invariance to      illumination, pose, and other variable conditions. This system was trained on the Labelled Faces in the wild(LFW) Dataset. This dataset contains more than 13,000 images of distinct faces collected from the web, and each face has a name (Label) to it.


   ### Triplet loss
   
   <a href="https://www.pluralsight.com/guides/face-recognition-walkthrough-facenet" target="blank"><img align="center" src="https://www.researchgate.net/profile/Zhenyao-Zhu/publication/316736728/figure/fig3/AS:491581309493249@1494213525316/The-Triplet-loss-in-cosine-similarity.png" alt="@waghhimanshu" height="200" width="450" /></a> 
   
This system employs a particular loss function called the triplet loss. The triplet loss minimizes the L2 distance between images of the same identity and maximizes the L2 distance between the face images of different characters.

The creators devised an efficient triplet selection mechanism which smartly selects three images at a time. These images are of the following three types:
1. **anchor :** an image of a random person.
2. **positive image :** another image of the same person.
3. **negative image :** an image of a different person.

Two Euclidean distances are measured: One between the anchor and the positive image, let’s call it A. Another between the anchor and the negative image, let’s call this B. The training process aims to reduce A and maximise B, such that similar images lie close to each other and distinct images lie far away in the embedding space.

Reference : https://towardsdatascience.com/s01e01-3eb397d458d
