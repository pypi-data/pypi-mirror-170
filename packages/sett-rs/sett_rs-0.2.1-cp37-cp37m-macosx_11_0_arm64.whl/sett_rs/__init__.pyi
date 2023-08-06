from typing import Sequence, Optional, Callable, Any

def sftp_upload(
    files: Sequence[str],
    host: str,
    username: str,
    destination_dir: str,
    envelope_dir: Optional[str] = None,
    pkey: Optional[str] = None,
    pkey_password: Optional[str] = None,
    progress: Optional[Callable[[float], Any]] = None,
    buf_size: Optional[int] = None,
    two_factor_callback: Optional[Callable[[], str]] = None,
) -> None: ...
def encrypt(
    files: Sequence[str],
    recipients: Sequence[str],
    sender: Optional[str],
    password: Optional[str],
    dry_run: bool,
    force: bool,
    output: Optional[str] = None,
    purpose: Optional[str] = None,
    transfer_id: Optional[int] = None,
    compression_level: Optional[int] = None,
    max_cpu: Optional[int] = None,
    progress: Optional[Callable[[float], Any]] = None,
) -> Optional[str]: ...
def decrypt(
    file: str,
    recipients: Sequence[str],
    signer: Optional[str],
    password: Optional[str],
    dry_run: bool,
    decrypt_only: bool,
    output: Optional[str] = None,
    max_cpu: Optional[int] = None,
    progress: Optional[Callable[[float], Any]] = None,
) -> Optional[str]: ...
