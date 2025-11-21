# 🚀 TitanIA Deployment Instructions

I have prepared all the scripts for you. Since I don't have access to your terminal's `aws` and `docker` commands directly, please run the following commands in your terminal:

## 0. Navigate to Project Folder
**First, run this command to go to the right folder:**
```bash
cd "/Users/vijay/Desktop/AI_ML Project/TitanIA"
```

## 0. Prerequisites (Fix "command not found" error)
**You are missing the AWS CLI.** Since you have Homebrew, run this first:
```bash
brew install awscli
```
Then verify it works:
```bash
aws --version
```

## 0.5 Configure Credentials (Fix "Unable to locate credentials")
You need to log in. Run this and enter your **Access Key** and **Secret Key**:
```bash
aws configure
```
*(Default Region: `us-east-1`, Output format: `json`)*

## 1. Navigate to Project Folder

```bash
# 1. Build the project
cd frontend
npm run build
cd ..

# 2. Create Bucket (Replace with a unique name)
aws s3 mb s3://titania-frontend-v1

# 3. Upload Files
aws s3 sync frontend/dist s3://titania-frontend-v1

# 4. Enable Website Hosting
aws s3 website s3://titania-frontend-v1 --index-document index.html
```
**Your URL:** `http://titania-frontend-v1.s3-website-us-east-1.amazonaws.com`

## 2. Deploy Backend (EC2)
1.  Launch an **EC2 t2.micro** instance.
2.  Copy the contents of `user_data.sh` into the **User Data** field during launch.
3.  Once running, SSH into it and run:
    ```bash
    docker-compose -f docker-compose.prod.yml up -d
    ```

## 3. Verify
Go to your frontend URL and try uploading a document!
