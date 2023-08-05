from typing import ClassVar, Sequence, Optional, List
from solders.instruction import Instruction, CompiledInstruction
from solders.pubkey import Pubkey
from solders.hash import Hash
from solders.address_lookup_table_account import AddressLookupTableAccount

class MessageHeader:
    LENGTH: ClassVar[int]
    def __init__(
        self,
        num_required_signatures: int,
        num_readonly_signed_accounts: int,
        num_readonly_unsigned_accounts: int,
    ) -> None: ...
    @staticmethod
    def default() -> "MessageHeader": ...
    @property
    def num_required_signatures(self) -> int: ...
    @property
    def num_readonly_signed_accounts(self) -> int: ...
    @property
    def num_readonly_unsigned_accounts(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "MessageHeader", op: int) -> bool: ...
    def __bytes__(self) -> bytes: ...
    @staticmethod
    def from_bytes(data: bytes) -> "MessageHeader": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "MessageHeader": ...

class Message:
    def __init__(
        self,
        instructions: Sequence[Instruction],
        payer: Optional[Pubkey] = None,
    ) -> None: ...
    @property
    def header(self) -> MessageHeader: ...
    @property
    def account_keys(self) -> List[Pubkey]: ...
    @property
    def recent_blockhash(self) -> Hash: ...
    @property
    def instructions(self) -> List[CompiledInstruction]: ...
    @staticmethod
    def new_with_blockhash(
        instructions: Sequence[Instruction], payer: Optional[Pubkey], blockhash: Hash
    ) -> "Message": ...
    @staticmethod
    def new_with_nonce(
        instructions: Sequence[Instruction],
        payer: Optional[Pubkey],
        nonce_account_pubkey: Pubkey,
        nonce_authority_pubkey: Pubkey,
    ) -> "Message": ...
    @staticmethod
    def new_with_compiled_instructions(
        num_required_signatures: int,
        num_readonly_signed_accounts: int,
        num_readonly_unsigned_accounts: int,
        account_keys: Sequence[Pubkey],
        recent_blockhash: Hash,
        instructions: Sequence[CompiledInstruction],
    ) -> "Message": ...
    def hash(self) -> Hash: ...
    @staticmethod
    def hash_raw_message(message_bytes: bytes) -> Hash: ...
    def compile_instruction(self, ix: Instruction) -> CompiledInstruction: ...
    def __bytes__(self) -> bytes: ...
    def program_id(self, instruction_index: int) -> Optional[Pubkey]: ...
    def program_index(self, instruction_index: int) -> Optional[int]: ...
    def program_ids(self) -> List[Pubkey]: ...
    def is_key_passed_to_program(self, key_index: int) -> bool: ...
    def is_key_called_as_program(self, key_index: int) -> bool: ...
    def is_non_loader_key(self, key_index: int) -> bool: ...
    def program_position(self, index: int) -> Optional[int]: ...
    def maybe_executable(self, i: int) -> bool: ...
    def is_writable(self, i: int) -> bool: ...
    def is_signer(self, i: int) -> bool: ...
    def signer_keys(self) -> List[Pubkey]: ...
    def has_duplicates(self) -> bool: ...
    @staticmethod
    def default() -> "Message": ...
    @staticmethod
    def from_bytes(data: bytes) -> "Message": ...
    def __richcmp__(self, other: "Message", op: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "Message": ...

class MessageAddressTableLookup:
    def __init__(
        self, account_key: Pubkey, writable_indexes: bytes, readonly_indexes: bytes
    ) -> None: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "MessageAddressTableLookup", op: int) -> bool: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "MessageAddressTableLookup": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "MessageAddressTableLookup": ...
    @property
    def account_key(self) -> Pubkey: ...
    @property
    def writable_indexes(self) -> bytes: ...
    @property
    def readonly_indexes(self) -> bytes: ...

class MessageV0:
    def __init__(
        self,
        header: MessageHeader,
        account_keys: Sequence[Pubkey],
        recent_blockhash: Hash,
        instructions: Sequence[CompiledInstruction],
        address_table_lookups: Sequence[MessageAddressTableLookup],
    ) -> None: ...
    @staticmethod
    def try_compile(
        payer: Pubkey,
        instructions: Sequence[Instruction],
        address_lookup_table_accounts: Sequence[AddressLookupTableAccount],
        recent_blockhash: Hash,
    ) -> "MessageV0": ...
    @property
    def header(self) -> MessageHeader: ...
    @property
    def account_keys(self) -> List[Pubkey]: ...
    @property
    def recent_blockhash(self) -> Hash: ...
    @property
    def instructions(self) -> List[CompiledInstruction]: ...
    @property
    def address_table_lookups(self) -> List[MessageAddressTableLookup]: ...
    def sanitize(self, reject_dynamic_program_ids: bool) -> None: ...
    def hash(self) -> Hash: ...
    @staticmethod
    def hash_raw_message(message_bytes: bytes) -> Hash: ...
    def __bytes__(self) -> bytes: ...
    def is_key_called_as_program(self, key_index: int) -> bool: ...
    def is_maybe_writable(self, key_index: int) -> bool: ...
    def is_non_loader_key(self, key_index: int) -> bool: ...
    def is_signer(self, index: int) -> bool: ...
    @staticmethod
    def default() -> "MessageV0": ...
    @staticmethod
    def from_bytes(data: bytes) -> "MessageV0": ...
    def __richcmp__(self, other: "MessageV0", op: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "MessageV0": ...
