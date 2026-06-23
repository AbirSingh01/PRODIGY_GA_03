from diffusers import StableDiffusionPipeline
import torch

print("Loading model...")

pipe = StableDiffusionPipeline.from_pretrained(
    "OFA-Sys/small-stable-diffusion-v0"
)

pipe = pipe.to("cuda")

prompt = "A futuristic smart city with flying cars at sunset"

print("Generating image...")

image = pipe(prompt).images[0]

image.save("generated_image.png")

print("Image generated successfully!")